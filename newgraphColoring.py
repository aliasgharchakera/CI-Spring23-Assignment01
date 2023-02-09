import random
import copy
import statistics
import matplotlib.pyplot as plt
import selection_scheme as ss
class graphColoring:
    
    def __init__(self, path, colors, n) -> None:
        self.colors = colors
        self.graph = self.read_graph_from_file(path)
        self.population_size = n
        self.population = self.generate_initial_population(self.population_size)
        
    def read_graph_from_file(self, file_name):
        graph = {}
        with open(file_name, 'r') as file:
            first = 1
            for line in file:
                line = line[1:].strip()
                if first:
                    line = line.split()
                    self.num = int(line[1])
                    first = 0
                else:
                    if line:
                        node1, node2 = map(int, line.split())
                        if node1 not in graph:
                            graph[node1] = []
                        if node2 not in graph:
                            graph[node2] = []
                        graph[node1].append(node2)
                        graph[node2].append(node1)
        return graph

    def fitness(self, coloring):
        # conflicts = 0
        colors = []
        for node, neighbors in self.graph.items():
            if coloring[node] not in colors:
                colors.append(coloring[node])
        return len(colors)
    
    def getFitness(self):
        lst = list()
        for i in self.population:
            lst.append(self.fitness(i))

    def generate_random_coloring(self):
        coloring = {}
        for node, neighbors in self.graph.items():
            coloring[node] = random.choice(self.colors)
            for neighbor in neighbors:
                try:
                    while coloring[node] == coloring[neighbor]:
                        coloring[node] = random.choice(self.colors)
                except:
                    coloring[node] = random.choice(self.colors)
        return coloring

    def generate_initial_population(self, population_size):
        population = dict()
        for i in range(population_size):
            # population.append(self.generate_random_coloring())
            coloring = self.generate_random_coloring()
            fitness = self.fitness(coloring)
            population[fitness] = coloring
        return population
    def createOffSpring(self, firstParent, secondParent, swap):
        
        offSpring1 = [0 for i in range(self.num)]
        weight1 = 0
        visited = []

        if (swap == True):
            _firstParent = secondParent
            _secondParent = firstParent
        else:
            _firstParent = firstParent
            _secondParent = secondParent

        for i in range(len(firstParent)//2):
            if (_firstParent[i][1] + weight1 <= self.capacity and _firstParent[i] not in visited):
                visited.append(_firstParent[i])
                offSpring1[i] = _firstParent[i]
                weight1 += _firstParent[i][1]

        i = len(firstParent) // 2
        for j in range(len(firstParent)//2):
            if (_secondParent[i+j][1] + weight1 <= self.capacity and _secondParent[i+j] not in visited):
                visited.append(_secondParent[i+j])
                offSpring1[i+j] = _secondParent[i+j]
                weight1 += _secondParent[i+j][1]
        
        for i in range(len(firstParent)//2):
            if (_secondParent[i][1] + weight1 <= self.capacity and _secondParent[i] not in visited):
                visited.append(_secondParent[i])
                offSpring1[i] = _secondParent[i]
                weight1 += _secondParent[i][1]
 
        i = len(firstParent) // 2
        for j in range(len(firstParent)//2):
            if (_firstParent[i+j][1] + weight1 <= self.capacity and _firstParent[i+j] not in visited):
                visited.append(_firstParent[i+j])
                offSpring1[i+j] = _firstParent[i+j]
                weight1 += _firstParent[i+j][1]        

        return weight1, offSpring1
    
    # def select_parents(self):
        

def main(graph:graphColoring, max_generations, mutation_probability):
    # population = graph.generate_initial_population(graph, colors, population_size)
    minlst, avglst, avgminlst, avgavglst = list(), list(), list(), list()
    for iterations in range(10):
        graph.generate_initial_population(1000)
        for generations in range(max_generations):
            for i in range(5):
                a1, a2 = ss.fitnessProportionalSelection(graph.population, 2, True)
                parent1, parent2 = graph.population[a1], graph.population[a2]
                crossover_point = random.randint(1, len(parent1) - 1)

                offSpringDetails = graph.createOffSpring(parent1, parent2, False)
                graph.population[offSpringDetails[0]] = offSpringDetails[1]

                offSpringDetails2 = graph.createOffSpring(parent1, parent2, True)
                graph.population[offSpringDetails2[0]] = offSpringDetails2[1]
            graph.population = ss.truncation(graph.population, 30, True)
            minlst.append(max(graph.getFitness()))
            avglst.append(statistics.mean(graph.getFitness()))
        avgminlst.append(statistics.mean(minlst))
        avgavglst.append(statistics.mean(avglst))
            # graph.population.sort(key=lambda x: graph.fitness(x))
            # if graph.fitness(graph.population[0]) == 0:
            #     return graph.population[0]
            # next_population = graph.population[:graph.population_size//2]
            # for i in range(1, graph.population_size//2):
            #     parent1, parent2 = random.sample(graph.population[:graph.population_size//2], 2)
            #     child = copy.deepcopy(parent1)
            #     # slice = random.randint(0, graph.num - 1)
            #     # child = parent1[]
            #     for node in graph.graph.keys():
            #         if random.random() < mutation_probability:
            #             child[node] = random.choice(colors)
            #     next_population.append(child)
            # graph.population = next_population
            # # print('Avg: ',statistics.mean(bruh.getFitness()))
    return avgminlst, avgavglst

colors = [i for i in range(150)]
graph = graphColoring("gcol1.txt", colors, 30)
print(main(graph, 2000, 0.5))
minlst, avglst = main()
plt.plot([i for i in range(1, 11)], minlst, label="max")
plt.plot([i for i in range(1, 11)], avglst, label="avg")
plt.xlabel('generation')
plt.title('Plot of average fitness against generations')
# plt.xlabel('iteration')
# plt.title('Plot of average fitness against iterations')
plt.ylabel('fitness')
plt.legend()
plt.show()
