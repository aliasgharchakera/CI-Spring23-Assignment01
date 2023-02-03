from evolutionaryalgo import *
import tsplib95 as tsp

class TSP:
    def __init__(self, path) -> None:
        file = tsp.load(path)
        graph = file.as_keyword_dict()
        print(graph)
        # for i, j in graph:
        #     print(i, j)
    def getFitness(self):
        pass
    def getPopulation(self):
        pass
    def chooseParent(self):
        pass
    
bruh = TSP("qa194.tsp")