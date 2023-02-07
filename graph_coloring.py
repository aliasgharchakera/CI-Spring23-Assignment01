import random
import copy

def read_graph_from_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        first = 1
        for line in file:
            if first:
                first = 0
            else:
                line = line[1:].strip()
                if line:
                    node1, node2 = map(int, line.split())
                    if node1 not in graph:
                        graph[node1] = []
                    if node2 not in graph:
                        graph[node2] = []
                    graph[node1].append(node2)
                    graph[node2].append(node1)
    return graph


def fitness(coloring, graph):
    conflicts = 0
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                conflicts += 1
    return conflicts

def generate_random_coloring(graph, colors):
    coloring = {}
    for node in graph.keys():
        coloring[node] = random.choice(colors)
    return coloring

def generate_initial_population(graph, colors, population_size):
    population = []
    for i in range(population_size):
        population.append(generate_random_coloring(graph, colors))
    return population

def genetic_algorithm(graph, colors, population_size, max_generations, mutation_probability):
    population = generate_initial_population(graph, colors, population_size)
    for generation in range(max_generations):
        population.sort(key=lambda x: fitness(x, graph))
        if fitness(population[0], graph) == 0:
            return population[0]
        next_population = [population[0]]
        for i in range(1, population_size):
            parent1, parent2 = random.sample(population[:population_size//2], 2)
            child = copy.deepcopy(parent1)
            for node in graph.keys():
                if random.random() < mutation_probability:
                    child[node] = random.choice(colors)
            next_population.append(child)
        population = next_population
    return None

graph = read_graph_from_file("gcol1.txt")
colors = ["red", "green", "blue"]
print(genetic_algorithm(graph, colors, 20, 1000, 0.5))
