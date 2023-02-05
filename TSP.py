from evolutionaryalgo import *
import random
import math
import tsplib95 as tsp

class TSP:

    def __init__(self, path, n) -> None:
        file = tsp.load(path)
        temp = file.as_keyword_dict()
        self.cities = temp['NODE_COORD_SECTION']
        self.dimension = temp['DIMENSION']
        # self.cities = {}
        # for i in range(194):
        #     self.cities[i] = self.graph[i+1]
        self.population = self.generatepopulation(self.dimension)
        #print(self.cities)
        # print(self.population)
        #print(self.num)
    
    def fitness(self, lst):
        fit = 0
        for i in range(len(lst)):
            if i != len(lst)-1:
                distance = self.getDistance(
                    self.cities[lst[i]], self.cities[lst[i+1]])
                fit += distance
        # doing this as it will complete the path by covering the distance from last node to first node.
        fit += self.getDistance(
            self.cities[len(lst)-1], self.cities[lst[0]])
        return fit

    def calculateFitness(self,tour:list):
        """
        Calculates the fitness of the self.population
        """
        # length = 0.0
        # self.fitnessValues = []
        # for i in range(len(self.population)):
        #     for j in range(len(self.population[i])-1):
        #         length += self.getDistance(self.cities[self.population[i][j]], self.cities[self.population[i][j+1]])
        #     self.fitnessValues.append(length)
        # return self.fitnessValues
        #10 cities
        #tour = [1,2,3,4,5,6,7,8,9,10]
        #cities = {'1':(x,y),2:(x,y)}
        length = 0
        for i in range(len(tour)-1):
            # print(self.cities[tour[i]], self.cities[tour[i+s1]])
            length += self.getDistance(self.cities[tour[i]], self.cities[tour[i+1]])
        
        #to return back to origin city    
        length += self.getDistance(self.cities[tour[len(tour)-1]], self.cities[tour[0]])
        return length

    def generatepopulation(self, n):
        """
        Generates a random initial self.population.
        """
        self.population = {}
        for i in range(1,n+1):
            done = list()
            for j in range(self.dimension):
                city = random.randint(1, self.dimension+1)
                while city in done:
                    city = random.randint(1, self.dimension+1)
                done.append(city)
            self.population[self.calculateFitness(done)] = done
        return self.population
        # chromo_dic = {}
        # for i in range(n):
        #     temp = list(range(194))
        #     random.shuffle(temp)
            
        #     while (tuple(temp) in chromo_dic):
        #         temp = list(range(194))
        #         random.shuffle(temp)
        #     chromo_dic[tuple(temp)] = self.fitness(temp)
        # return chromo_dic
        # generateCount = n
        # for i in range(generateCount):                  
        #     tour = list(range(194))
        #     random.shuffle(tour)
        #     self.population.append(tour)
        # return self.population
    
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

        # tempPop = [offspring1,offspring2]
        # tempLength = self.calculateFitness(tempPop)
        # self.fitnessValues.append(tempLength[0])
        # self.fitnessValues.append(tempLength[1])

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

    def fitnessProportionalSurvivalSelection(self)->list:
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
        self.population = self.parents



# bruh = TSP("qa194.tsp", 10)
# bruh.calculateFitness()
# bruh.getOffspring()
# bruh.fitnessProportionalSurvivalSelection()
# print(bruh.calculateFitness())

def main():
    bruh = TSP('qa194.tsp',10)
    print(bruh.calculateFitness())
    # for i in range(100000):
        # bruh.calculateFitness()
        # for i in range(100):
            # bruh.getOffspring()
        # bruh.fitnessProportionalSurvivalSelection()
    # print(bruh.calculateFitness())

main()



# population = bruh.getPopulation()
# bruh.calculateFitness(population)
# bruh.getOffspring()
# print(bruh.get_fitness())
