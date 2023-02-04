from evolutionaryalgo import *
import random
import math
import tsplib95 as tsp

class TSP:
    def __init__(self, path, n) -> None:
        file = tsp.load(path)
        temp = file.as_keyword_dict()
        self.graph = temp['NODE_COORD_SECTION']
        self.num = temp['DIMENSION']
        self.fitnessValues = []
        # print(self.graph)
        self.population = self.generatepopulation(n)
        #print(self.population)
        #print(self.graph)
        self.cities = {}
        for i in range(194):
            self.cities[i] = self.graph[i+1]

    def calculateFitness(self,population:list):
        """
        Calculates the fitness of the self.population
        """
        # for i in self.self.population:
        #     self.fitness = self.__getFitness(i)
        length = 0.0
        self.fitnessValues = []
        for i in range(len(population)):
            for j in range(len(population[i])-1):
                length += self.getDistance(self.cities[population[i][j]], self.cities[population[i][j+1]])
            self.fitnessValues.append(length)
        return self.fitnessValues
    
    # def __getFitness(self, lst: list):
    #     """returns the fitness value for the self.population

    #     Args:
    #         lst (list): self.population
    #     """
    #     length = 0
    #     for i in range(len(lst)):
    #         length += tsp.getD

    def generatepopulation(self, n):
        """
        Generates a random initial self.population.
        """
        self.population = list()
        # for i in range(n):
        #     done = list()
        #     for j in range(1, self.num + 1):
        #         city = random.randint(1, self.num)
        #         while city in done:
        #             city = random.randint(1, self.num)
        #         done.append(city)
        #     self.population.append(done)
        # return self.population
        generateCount = n
        for i in range(generateCount):                  
            tour = list(range(194))
            random.shuffle(tour)
            self.population.append(tour)
        return self.population
    
    def chooseParents(self):
        """
        Implements a parent selection criteria
        
        Returns the selected pair
        """
        pass
    
    def getOffspring(self):
        """Implement Crossover and Mutation

        Args:
            parents (list): list of parents
        """
        firstParent = self.fitnessProportionalSelection()[0]
        secondParent = self.fitnessProportionalSelection()[0]

        crossover_point = random.randint(1, len(firstParent) - 1)
        offspring1 = firstParent[:crossover_point] + secondParent[crossover_point:]
        offspring2 = secondParent[:crossover_point] + firstParent[crossover_point:]

        # Repair offspring to make them valid tours
        offspring1 = self.repair(offspring1)
        offspring2 = self.repair(offspring2)

        tempPop = [offspring1,offspring2]
        tempLength = self.calculateFitness(tempPop)
        self.fitnessValues.append(tempLength[0])
        self.fitnessValues.append(tempLength[1])

        self.population.append(offspring1)
        self.population.append(offspring2)
    
    def repair(self,offspring:str):
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
    
    def getPopulation(self):
        return self.population

    # def crossOver(self, parents: list):
    #     """
    #     Produces offspring through crossover of parents
        
    #     Returns the offsprings
    #     """
    #     pass
    
    # def mutation(self):
    #     """
    #     Mutates the offspring
        
    #     Returns the mutated individual
    #     """
    #     pass    

    def getDistance(self,c1:list, c2:list)->float:
        return math.sqrt((c1[0]-c2[0])**2) + ((c1[1]-c2[1])**2)
    
    def fitnessProportionalSelection(self)->list:
    #reference: CHATGPT
        totalFitness = sum(self.fitnessValues)
        normalized_fitness = [f/totalFitness for f in self.fitnessValues]
        CDF = [normalized_fitness[0]]
        for i in range(1, len(normalized_fitness)):
            CDF.append(CDF[-1] + normalized_fitness[i])
        self.parents = []
        for i in range(len(self.population)):
            r = random.random()
            for j, f in enumerate(CDF):
                # print(j)
                if r <= f:
                    if (self.population[j]) not in self.parents:
                        self.parents.append(self.population[j])
                        break
            if (len(self.parents)) > 0:
                break 
        return self.parents

bruh = TSP("qa194.tsp", 10)
population = bruh.getPopulation()
bruh.calculateFitness(population)
bruh.getOffspring()