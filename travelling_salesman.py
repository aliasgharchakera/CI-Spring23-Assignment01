
import tsplib95 as tsp
import math
import random

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
        self.population = self.generatepopulation(n)

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
            totalDistance += self.calculateEucDistance(tour[i],tour[i+1])
        #Adding distance back to the origin
        totalDistance += self.calculateEucDistance(tour[len(tour)-1],tour[0])
        return round(totalDistance,2)
    
    def generatepopulation(self, n):
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






    
    