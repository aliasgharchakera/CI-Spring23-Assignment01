
import tsplib95 as tsp
import math
import random
import statistics
import selection_scheme as ss

class TSP:
    
    def __init__(self, path, n) -> None:
        '''
        Constructor for class TSP that loads .tsp file
        self.cities = {1:(x,y),2:(x,y).....}
        self.dimension = number of cities
        self.population = candidate solutions = [[candidate sol 1], [candidate sol 2]]
        '''
        file = tsp.load(path)
        temp = file.as_keyword_dict()
        self.cities = temp['NODE_COORD_SECTION']
        self.dimension = temp['DIMENSION']
        self.population = self.generatePopulation(n)
        self.n = n
        #print(self.population.keys())
        #print('-----')

    def calculateEucDistance(self, c1, c2):
        '''
        Calculates Euclidean distance between two coordinates c1 and c2.
        '''
        return math.sqrt(math.pow(c1[0]-c2[0],2) + math.pow(c1[1]-c2[1],2))

    def calculateFitness(self, tour:list):
        '''
        Calculates fitness for a single tour around Qatar. 
        tour = [1,2,3,4,5,...,194]
        '''
        totalDistance = 0
        for i in range(len(tour)-1):
            totalDistance += self.calculateEucDistance(self.cities[tour[i]],self.cities[tour[i+1]])
        #Adding distance back to the origin
        totalDistance += self.calculateEucDistance(self.cities[tour[len(tour)-1]],self.cities[tour[0]])
        return round(totalDistance,2)
    
    def generatePopulation(self, n):
        """
        Generates a random initial self.population.
        """
        self.population = {}
        for i in range(n):
            done = list()
            for j in range(self.dimension):
                city = random.randint(1, self.dimension)
                while city in done:
                    city = random.randint(1, self.dimension)
                done.append(city)
            self.population[self.calculateFitness(done)] = done
        return self.population

    def selectParents(self):
        '''
        will select two parents randomly from the population
        '''
        #random selection of parents
        parents = ss.randomSelection(self.population,2)
        return parents[0], parents[1]

        #Parents selection from fitness proportional share
        # parents = ss.fitnessProportionalSelection(self.population,2)
        # return parents[0], parents[1]
        
        #Parents selection from rank based 
        # parents = ss.rankBaseSelection(self.population,30,True)
        # return parents[0], parents[1]

        # return ss.binaryTournament(self.population), ss.binaryTournament(self.population)
        
    def crossOver(self):
        '''
        This function will do crossover of two parents
        '''
        populationDctKeys = self.selectParents()
        firstParent = self.population[populationDctKeys[0]]
        secondParent = self.population[populationDctKeys[1]]
        
        crossover_point = random.randint(1, len(firstParent) - 1)

        offspring1 = firstParent[:crossover_point] + secondParent[crossover_point:]
        offspring2 = secondParent[:crossover_point] + firstParent[crossover_point:]
 
        offspring1 = self.repair(offspring1)
        offspring2 = self.repair(offspring2)
        
        offspring1 = self.mutate(offspring1,0.5)
        offspring2 = self.mutate(offspring2,0.5)

        self.population[self.calculateFitness(offspring1)] = offspring1
        self.population[self.calculateFitness(offspring2)] = offspring2

    def repair(self,offspring):
        '''
        Will repair the offspring in case of repitition of any cities.
        '''
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

    def mutate(self,offspring:str,probability:float):
        '''
        It will do a coin toss to match the probability. 
        Will make changes in offspring by swapping at various indexes.
        '''
        coinToss = random.random()
        while(coinToss <= probability):
            coinToss = random.random()
            length = len(offspring)
            changePoint = random.randint(0,length-1)
            changePoint1 = random.randint(0,length-1)
            while(changePoint == changePoint1):
                changePoint1 = random.randint(0,length-1)
            offspring[changePoint],offspring[changePoint1] = offspring[changePoint1], offspring[changePoint]
        return offspring

    def survivalSelection(self):
        self.population = ss.truncation(self.population,self.n, False)
        #self.population = ss.rankBaseSelection(self.population,50,False)
        # self.population = ss.fitnessProportionalSelection(self.population,50,False)
        # self.population = ss.randomSelection(self.population,30)
    
    def getFitness(self):
        return list(self.population.keys())
    
def main():
    bruh = TSP('qa194.tsp',30)
    # bruh.crossOver()
    for i in range(1):
        for i in range(40):
            for i in range(5):
                bruh.crossOver()
            bruh.survivalSelection()
            print('Max: ',max(bruh.getFitness()))
            print('Avg: ',statistics.mean(bruh.getFitness()))
    #print(bruh.getFitness())

main()
    

        





    
    