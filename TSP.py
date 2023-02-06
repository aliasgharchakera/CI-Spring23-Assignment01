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
        self.population = self.generatepopulation(n)

        #print(self.cities)
        # print(self.population)
        #print(self.num)

    def getDistance(self,c1:list, c2:list)->float:
        return math.sqrt(math.pow(c1[0]-c2[0],2) + math.pow(c1[1]-c2[1],2))

    def calculateFitness(self):
        """
        Calculates the fitness of the self.population
        """
        length = 0
        self.fitnessValues = []
        for i in range(len(self.population)):
            length = 0
            for j in range(len(self.population[i])-1):
                length += self.getDistance(self.cities[self.population[i][j]], self.cities[self.population[i][j+1]])
            length += self.getDistance(self.cities[self.population[i][len(self.population[i])-1]], self.cities[self.population[i][0]])
            self.fitnessValues.append(length)
        return self.fitnessValues
        #10 cities
        #tour = [1,2,3,4,5,6,7,8,9,10]
        #cities = {'1':(x,y),2:(x,y)}
        # length = 0
        # for i in range(len(tour)-1):
        #     # print(self.cities[tour[i]], self.cities[tour[i+s1]])
        #     length += self.getDistance(self.cities[tour[i]], self.cities[tour[i+1]])
        
        # # #to return back to origin city    
        # length += self.getDistance(self.cities[tour[len(tour)-1]], self.cities[tour[0]])
        # return length

    def generatepopulation(self, n):
        """
        Generates a random initial self.population.
        """
        self.population = list()
        for i in range(n):
            done = list()
            for j in range(self.dimension):
                city = random.randint(1, self.dimension)
                while city in done:
                    city = random.randint(1, self.dimension)
                done.append(city)
            self.population.append(done)
            # self.population.append(done)
        return self.population
    
    # def getOffspring(self):
    #     """Implement Crossover and Mutation

    #     Args:
    #         parents (list): list of parents
    #     """
    #     # firstParent = self.fitnessProportionalSelection()[0]
    #     # secondParent = self.fitnessProportionalSelection()[0]
    #     parents = self.selectParents()
    #     firstParent = parents[0]
    #     secondParent = parents[1]
    #     crossover_point = random.randint(1, len(firstParent) - 1)
    #     # print(crossover_point)
    #     offspring1 = firstParent[:crossover_point] + secondParent[crossover_point:]
    #     offspring2 = secondParent[:crossover_point] + firstParent[crossover_point:]

    #     offspring1 = self.repair(offspring1)
    #     offspring2 = self.repair(offspring2)

    #     self.population.append(offspring1)
    #     self.population.append(offspring2)
    
    def repair(self,offspring:str):
        tour = []
        visited = [False] * (len(offspring)+1)
        for i in range(len(offspring)):
            if not visited[offspring[i]]:
                tour.append(offspring[i])
                visited[offspring[i]] = True
        for i in range(1,len(offspring)+1):
            if not visited[i]:
                tour.append(i)
        return tour


    
    # def fitnessProportionalSelection(self)->list:
    
    #     totalFitness = sum(self.fitnessValues)
    #     normalized_fitness = [f/totalFitness for f in self.fitnessValues]
    #     CDF = [normalized_fitness[0]]
    #     for i in range(1, len(normalized_fitness)):
    #         CDF.append(CDF[-1] + normalized_fitness[i])
    #     self.parents = []
    #     for i in range(len(self.population)):
    #         r = random.random()
    #         for j, f in enumerate(CDF):
    #             # print(j)
    #             if r <= f:
    #                 if (self.population[j]) not in self.parents:
    #                     self.parents.append(self.population[j])
    #                     break
    #         if (len(self.parents)) > 0:
    #             break 
    #     return self.parents

    def fitnessProportionalSurvivalSelection(self)->list:

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

    def selectParents(self):
        '''
        Selecting the most best candidate as a parent
        '''
        tempLst = self.fitnessValues
        tempLst.sort()
        firstMaxFitness = tempLst[len(tempLst)-1]
        secondMaxFitness = tempLst[len(tempLst)-2]
        firstPopulationIndex = self.fitnessValues.index(firstMaxFitness)
        secondPopulationIndex = self.fitnessValues.index(secondMaxFitness)
        firstParent = self.population[firstPopulationIndex]
        secondParent = self.population[secondPopulationIndex]
        return [firstParent,secondParent]

    def breed(self,parents, offspring_size):
        """
        Create a new generation of offspring by combining the values of the parents.
        """
        offspring = []
        for i in range(offspring_size):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            offspring.append([(parent1[j] + parent2[j]) //
                             2 for j in range(len(parent1))])
        return offspring

    def mutate(self,offspring, mutation_probability):
        """
        Introduce random mutations into the offspring to promote genetic diversity.
        """
        for i in range(len(offspring)):
            for j in range(len(offspring[i])):
                if random.random() < mutation_probability:
                    offspring[i][j] = random.randint(1, 194)
        return offspring

    def getOffsprings(self):
        offspring = self.breed(self.selectParents(),2)
        offspring = self.mutate(offspring,0.6)

        offspring1 = self.repair(offspring[0])
        offspring2 = self.repair(offspring[1])

        self.population.append(offspring1)
        self.population.append(offspring2)
    



    

    def rankBasedSelection(self):
        pass




def main():
    bruh = TSP('qa194.tsp',10)
    #print(bruh.fitness_proportional())
    # print(bruh.calculateFitness())
    # bruh.getOffspring()
    # print(bruh.calculateFitness())
    bruh.calculateFitness()
    for i in range(10000):
        for i in range(10):
            bruh.getOffsprings()
            bruh.calculateFitness()
        # bruh.getOffspring()
        bruh.fitnessProportionalSurvivalSelection()
    print(bruh.calculateFitness())

main()



