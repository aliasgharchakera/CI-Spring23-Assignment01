
import random

def rouletteWheelSelection(self):
    pass

def truncation(population:dict,n:int):
    '''
    It will sort the population based on fitness values and truncate the ones with lowest fitness.
    '''
    newDct = {}
    keysLst = list(population.keys())
    keysLst.sort()
    lengthOfPopulation = len(keysLst)
    shortListedKeys = list()
    j = 0
    for i in keysLst:
        shortListedKeys.append(i)
        j += 1
        if (j >= n):
            break
    random.shuffle(shortListedKeys)
    for i in shortListedKeys:
        newDct[i] = population[i]
    return newDct

def fitnessProportionalSelection(population:dict)->list:

    fitnessValues = list(population.keys()) 
    totalFitness = sum(fitnessValues)
    normalized_fitness = [f/totalFitness for f in fitnessValues]
    CDF = [normalized_fitness[0]]
    for i in range(1, len(normalized_fitness)):
        CDF.append(CDF[-1] + normalized_fitness[i])
    parents = []
    for i in range(len(population)):
        r = random.random()
        for j, f in enumerate(CDF):
            # print(j)
            if r <= f:
                if (fitnessValues[j]) not in parents:
                    parents.append(fitnessValues[j])
                    break
        if (len(parents)) > 1:
            break 
    return parents

import random

def order_crossover(parent1, parent2):
    length = len(parent1)
    c1, c2 = [0] * length, [0] * length
    # Select two random crossover points
    cx_point1 = random.randint(0, length - 1)
    cx_point2 = random.randint(0, length - 1)
    # Ensure that cx_point1 is always less than cx_point2
    if cx_point2 < cx_point1:
        cx_point1, cx_point2 = cx_point2, cx_point1
    # Copy the selected portion from parent1 to offspring1
    c1[cx_point1:cx_point2 + 1] = parent1[cx_point1:cx_point2 + 1]
    # Fill the remaining positions with cities from parent2, maintaining order
    p2_index = cx_point2 + 1
    for i in range(length):
        if parent2[p2_index % length] not in c1:
            c1[i] = parent2[p2_index % length]
            p2_index += 1
    # Repeat the process to generate offspring2
    c2[cx_point1:cx_point2 + 1] = parent2[cx_point1:cx_point2 + 1]
    p1_index = cx_point2 + 1
    for i in range(length):
        if parent1[p1_index % length] not in c2:
            c2[i] = parent1[p1_index % length]
            p1_index += 1
    return c1, c2

def mutation(offspring, mutation_rate):
    length = len(offspring)
    for i in range(length):
        if random.uniform(0, 1) < mutation_rate:
            swap_index = random.randint(0, length - 1)
            offspring[i], offspring[swap_index] = offspring[swap_index], offspring[i]
    return offspring