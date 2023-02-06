from evolutionaryalgo import *
import random

class Knapsack:
    def __init__(self, path, n) -> None:
        self.things = dict()
        self.stuff = list()
        with open(path) as f:
            lines = f.readlines()
            self.num, self.capacity = lines[0].split()
            self.num, self.capacity = int(self.num), int(self.capacity)
            for i in lines[1::]:
                value, weight = i.split()
                self.things[int(value)] = int(weight)
                self.stuff.append((int(value), int(weight)))
                # print(value, weight)
            # print(self.num)
            # print(self.capacity)
            # print(list(self.things))
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
        sum = 0
        # for i in range(n):
        #     done = dict()
        #     while sum < self.capacity:
        #         n = random.randint(0, self.num - 1)
        #         item = list(self.things)[n]
        #         value = list(self.things.values())[n]
        #         try:
        #             done[item] += value
        #         except: done[item] = value
        #         sum += value
        #     population.append(done)
        for i in range(n):
            done = dict()
            sum = 0
            while sum < self.capacity:
                n = random.randint(0, self.num - 1)
                weight = self.stuff[n][1]
                value = self.stuff[n][0]
                sum += weight
                if sum > self.capacity:
                    break
                try: done[n] = (weight, done[n] + value)
                except: done[n] = (weight, value)
            print(sum)
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
    
bruh = Knapsack("f8_l-d_kp_23_10000", 10)