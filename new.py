import random

def graph_coloring(graph):
    num_colors = len(graph)
    population_size = 10
    population = [random.sample(range(num_colors), num_colors) for _ in range(population_size)]
    fitness_scores = [calc_fitness(graph, coloring) for coloring in population]
    best_coloring = population[fitness_scores.index(max(fitness_scores))]

    num_generations = 10
    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size):
            parent_1 = random.choice(population)
            parent_2 = random.choice(population)
            child = crossover(parent_1, parent_2)
            new_population.append(mutate(child))

        population = new_population
        fitness_scores = [calc_fitness(graph, coloring) for coloring in population]
        best_coloring = population[fitness_scores.index(max(fitness_scores))]

    print(best_coloring)

def calc_fitness(graph, coloring):
    # fitness is calculated by counting the number of edges
    # that are not colored with the same color
    fitness = 0
    for node_a, node_b in graph:
        if coloring[node_a] != coloring[node_b]:
            fitness += 1
    return fitness

def mutate(coloring):
    # randomly change the color of one node
    node = random.randint(0, len(coloring)-1)
    coloring[node] = random.randint(0, len(coloring)-1)
    return coloring

def crossover(parent_1, parent_2):
    # randomly choose a crossover point
    crossover_point = random.randint(1, len(parent_1)-1)
    # create child by combining the two parents
    child = parent_1[:crossover_point] + parent_2[crossover_point:]
    return child

def read_graph_from_file(file_name):
        graph = list()
        with open(file_name, 'r') as file:
            first = 1
            for line in file:
                if first:
                    first = 0
                else:
                    line = line[1:].strip()
                    if line:
                        node1, node2 = map(int, line.split())
                        graph.append((node1, node2))
                        # if node1 not in graph:
                        #     graph[node1] = []
                        # if node2 not in graph:
                        #     graph[node2] = []
                        # graph[node1].append(node2)
                        # graph[node2].append(node1)
        return graph

if __name__ == '__main__':
    graph = read_graph_from_file('gcol1.txt')
    # print(graph)
    graph_coloring(graph)