
import random
import readingTSP
numCities = 194

cities = readingTSP.read_tsp('qa194.tsp')

def findDistance(c1:tuple, c2:tuple)->float:
    return ((c1[0]-c2[0])**2) + ((c1[1]-c2[1])**2)

def initialize_population(numCities:int)->list:
    generateCount = 20
    population = []
    for i in range(generateCount):
        tour = list(range(numCities))
        random.shuffle(tour)
        population.append(tour)
    return population

def findLengthOfTours(population:list,cities:dict)->list:
    length = 0.0
    lengthTours = []
    for i in range(len(population)):
        for j in range(len(population[i])-1):
            length += findDistance(cities[population[i][j]], cities[population[i][j+1]])
        lengthTours.append(length)
    return lengthTours

def fitnessProportionalSelection(population:list, fitness_values:list)->list:
    totalFitness = sum(fitness_values)
    normalized_fitness = [f/totalFitness for f in fitness_values]
    CDF = [normalized_fitness[0]]
    for i in range(1, len(normalized_fitness)):
        CDF.append(CDF[-1] + normalized_fitness[i])
    parents = []
    for i in range(len(population)):
        r = random.random()
        for j, f in enumerate(CDF):
            # print(j)
            if r <= f:
                if (population[j]) not in parents:
                    parents.append(population[j])
                    break
    return parents




    

population = initialize_population(194)
length = findLengthOfTours(population, cities)
print(len(fitnessProportionalSelection(population,length)))