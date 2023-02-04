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
        # print(self.graph)
        self.population = self.generatepopulation(n)
        #print(self.population)
        #print(self.graph)
        self.cities = {}
        for i in range(194):
            self.cities[i] = self.graph[i+1]

    def calculateFitness(self):
        """
        Calculates the fitness of the self.population
        """
        # for i in self.self.population:
        #     self.fitness = self.__getFitness(i)
        length = 0.0
        lengthTours = []
        for i in range(len(self.population)):
            for j in range(len(self.population[i])-1):
                length += self.getDistance(self.cities[self.population[i][j]], self.cities[self.population[i][j+1]])
            lengthTours.append(length)
        return lengthTours
    
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
    
    def getOffspring(self, parents: list):
        """Implement Crossover and Mutation

        Args:
            parents (list): list of parents
        """
        pass
    
    def crossOver(self, parents: list):
        """
        Produces offspring through crossover of parents
        
        Returns the offsprings
        """
        pass
    
    def mutation(self):
        """
        Mutates the offspring
        
        Returns the mutated individual
        """
        pass    

    def getDistance(self,c1:list, c2:list)->float:
        return math.sqrt((c1[0]-c2[0])**2) + ((c1[1]-c2[1])**2)
    
bruh = TSP("qa194.tsp", 10)
print(bruh.calculateFitness())