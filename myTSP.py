from evolutionaryalgo import *
import random
import tsplib95 as tsp

class TSP:
    def __init__(self, path, n) -> None:
        file = tsp.load(path)
        temp = file.as_keyword_dict()
        self.graph = temp['NODE_COORD_SECTION']
        self.num = temp['DIMENSION']
        # print(self.graph)
        self.population = self.generatePopulation(n)
        print(self.population)
        
    def calculateFitness(self):
        """
        Calculates the fitness of the population
        """
        for i in self.population:
            self.fitness = self.__getFitness(i)
    
    def __getFitness(self, lst: list):
        """returns the fitness value for the population

        Args:
            lst (list): population
        """
        for i in range(len(lst)):
            pass

    def generatePopulation(self, n):
        """
        Generates a random initial population.
        """
        population = list()
        for i in range(n):
            done = list()
            for j in range(1, self.num + 1):
                city = random.randint(1, self.num)
                while city in done:
                    city = random.randint(1, self.num)
                done.append(city)
            population.append(done)
        return population
    
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
    
bruh = TSP("qa194.tsp", 10)