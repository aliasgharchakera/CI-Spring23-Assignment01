
import random
import readingTSP
import math
numCities = 194

cities = readingTSP.read_tsp('qa194.tsp')
print(cities)

def findDistance(c1:tuple, c2:tuple)->float:
    return math.sqrt((c1[0]-c2[0])**2) + ((c1[1]-c2[1])**2)

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
    #reference: CHATGPT
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
        if (len(parents)) > 0:
            break 
    return parents


def crossOver(population:list,fitness_values:list,cities:dict):
    firstParent = fitnessProportionalSelection(population,fitness_values)[0]
    secondParent = fitnessProportionalSelection(population,fitness_values)[0]

    crossover_point = random.randint(1, len(firstParent) - 1)
    offspring1 = firstParent[:crossover_point] + secondParent[crossover_point:]
    offspring2 = secondParent[:crossover_point] + firstParent[crossover_point:]

    # Repair offspring to make them valid tours
    offspring1 = repair(offspring1)
    offspring2 = repair(offspring2)

    tempPop = [offspring1,offspring2]
    tempLength = findLengthOfTours(tempPop,cities)
    fitness_values.append(tempLength[0])
    fitness_values.append(tempLength[1])

    population.append(offspring1)
    population.append(offspring2)
    
    return fitness_values
    #return offspring1, offspring2

def repair(offspring:str):
    tour = []
    visited = [False] * len(offspring)
    for i in range(len(offspring)):
        if not visited[offspring[i]]:
            tour.append(offspring[i])
            visited[offspring[i]] = True
    for i in range(len(offspring)):
        if not visited[i]:
            tour.append(i)
    return tour

    

# population = initialize_population(194)
# #print(population)
# length = findLengthOfTours(population, cities)
# #print(length)
# print(len(crossOver(population,length,cities)))

# print(len(fitnessProportionalSelection(population,length)))

# def main():
#     population = initialize_population(194)
#     length = findLengthOfTours(population, cities)
#     for i in range(10):
#         crossOver(population,length)

    
