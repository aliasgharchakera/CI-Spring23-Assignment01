
import random

def binaryTournament(self,population:dict):
    
    lstDctKeys = list(population.keys())
    firstKey = lstDctKeys[random.randint(0,len(lstDctKeys)-1)]
    secondKey = lstDctKeys[random.randint(0,len(lstDctKeys)-1)]
    if (firstKey < secondKey):
        return secondKey
    return firstKey

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


def repairFitnessValues(fitnessValues:list)->list:
    newLst = []
    for i in fitnessValues:
        newLst.append(100000-i)
    return newLst

def fitnessProportionalSelection(population:dict)->list:

    fitnessValues = list(population.keys()) 
    repairedFitnessValues = repairFitnessValues(fitnessValues)
    totalFitness = sum(repairedFitnessValues)
    normalized_fitness = [f/totalFitness for f in repairedFitnessValues]
    CDF = [normalized_fitness[0]]
    for i in range(1, len(normalized_fitness)):
        CDF.append(CDF[-1] + normalized_fitness[i])
    parents = []
    for i in range(len(population)):
        r = random.random()
        for j, f in enumerate(CDF):
            # print(j)
            if r <= f:
                if (repairedFitnessValues[j]) not in parents:
                    parents.append(fitnessValues[j])
                    break
        if (len(parents)) > 1:
            break 
    return parents

def rankBaseSelection(population:dict):
    pass



