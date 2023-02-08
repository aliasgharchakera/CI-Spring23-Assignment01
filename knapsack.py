from evolutionaryalgo import *
import random



class Sack:
    def __init__(self, n) -> None:
        # self.value = value
        # self.weight = weight
        # self.items = list()
        self.weight = 0
        self.value = 0
        self.items = dict()
        self.__initializeSack(n)
        self.__calculateWV()
        #print(self.items)
        
    def __initializeSack(self, n):
        for i in range(n):
            self.items[i] = (0, 0)
    
    def __calculateWV(self):
        for i, j in self.items.items():
            self.weight += j[0]
            self.value += j[1]
    
    def insert(self, item, n):
        # self.items.append(item)
        self.items[n] = (item[0], self.items[n][1] + item[1])
        # except: self.items[n] = (item[0], item[1])
        self.weight += item[0]
        self.value += item[1]

class Knapsack:
    def __init__(self, path, n) -> None:
        self.things = dict()
        self.stuff = list()  #(weight, value)
        self.fitness = list()
        with open(path) as f:
            lines = f.readlines()
            self.num, self.capacity = lines[0].split()
            self.num, self.capacity = int(self.num), int(self.capacity)
            for i in lines[1::]:
                value, weight = i.split()
                self.things[int(value)] = int(weight)
                self.stuff.append((int(weight), int(value)))
                # print(value, weight)
            # print(self.num)
            # print(self.capacity)
            # print(list(self.things))
        # print(self.graph)
        self.population = self.generatePopulation(n)
        # print(self.population[0].items)
        #self.calculateFitness()
        # print(self.population)
        
    def calculateFitness(self):
        """
        Calculates the fitness of the population
        """
        for i in self.population:
            self.fitness.append(i.value)
    
    # def __getFitness(self, sack: Sack):
    #     """returns the fitness value for the population

    #     Args:
    #         lst (list): population
    #     """
    #     for i in range(len(lst)):
    #         pass

    def generatePopulation(self, n):
        """
        Generates a random initial population.
        """
        population = dict()
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
        # for i in range(n):
        #     done = dict()
        #     sum = 0
        #     while sum < self.capacity:
        #         n = random.randint(0, self.num - 1)
        #         weight = self.stuff[n][0]
        #         value = self.stuff[n][1]
        #         sum += weight
        #         if sum > self.capacity:
        #             break
                # try: done[n] = (weight, done[n] + value)
                # except: done[n] = (weight, value)
        #     print(sum)
        #     population.append(done)
        for i in range(n):
            weight = 0
            items = []
            #sack = Sack(self.num)
            while weight < self.capacity:
                k = random.randint(0, self.num - 1)
                if weight + self.stuff[k][0] > self.capacity:
                    break
                items.append(self.stuff[k])
                weight += self.stuff[k][0]
                #sack.insert(self.stuff[k], k)
            # print(sack.value, sack.weight)
            # population.append(sack)
            population[weight] = items
        return population
    
    def chooseParents(self):
        """
        Implements a parent selection criteria
        
        Returns the selected pair
        """
        # max = 0
        # j = 0
        # maxJ = 0
        # for i in self.fitness:
        #     if i > max:
        #         max = i
        #         maxJ = j
        #     j += 1

                
    
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