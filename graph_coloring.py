import random
import copy
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
                    self.num = line[1]
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
        conflicts = 0
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                if coloring[node] == coloring[neighbor]:
                    conflicts += 1
        return conflicts

    def generate_random_coloring(self):
        coloring = {}
        for node in self.graph.keys():
            coloring[node] = random.choice(self.colors)
        return coloring

    def generate_initial_population(self, population_size):
        population = []
        for i in range(population_size):
            population.append(self.generate_random_coloring())
        return population
    
    # def select_parents(self):
        

def genetic_algorithm(graph:graphColoring, max_generations, mutation_probability):
    # population = graph.generate_initial_population(graph, colors, population_size)
    for generation in range(max_generations):
        graph.population.sort(key=lambda x: graph.fitness(x))
        if graph.fitness(graph.population[0]) == 0:
            return graph.population[0]
        next_population = graph.population[:graph.population_size//2]
        for i in range(1, graph.population_size//2):
            parent1, parent2 = random.sample(graph.population[:graph.population_size//2], 2)
            child = copy.deepcopy(parent1)
            # slice = random.randint(0, graph.num - 1)
            # child = parent1[]
            for node in graph.graph.keys():
                if random.random() < mutation_probability:
                    child[node] = random.choice(colors)
            next_population.append(child)
        graph.population = next_population
    return None

# def main(graph, colors, population_size, max_generations, mutation_probability):
#     population = generate_initial_population(graph, colors, population_size)
#     for generation in range(max_generations):
#         population.sort(key=lambda x: fitness(x, graph))
#         i = 0
#         while fitness(population[i], graph) != 0 and i < population_size:
#             i += 1
#         if i != population_size:
#             return population[i]
#         # if fitness(population[0], graph) == 0:
#         #     return population[0]
#         next_population = [population[0]]
#         for i in range(1, population_size):
#             parent1, parent2 = random.sample(population[:population_size//2], 2)
#             child = copy.deepcopy(parent1)
#             for node in graph.keys():
#                 if random.random() < mutation_probability:
#                     child[node] = random.choice(colors)
#             next_population.append(child)
#         population = next_population
#     return None

colors = [i for i in range(150)]
graph = graphColoring("gcol1.txt", colors, 30)
print(genetic_algorithm(graph, 2000, 0.5))
