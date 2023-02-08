import random


class Graph:
    def __init__(self, filename: str, numColours: int, mutation_prob: float, size: int, gens) -> None:
        self.vertices = 0
        self.population = []
        self.mutationRate = mutation_prob
        self.numColours = numColours
        self.populationSize = size
        self.generations = gens
        self.graph = self.read_graph(filename)

    def read_graph(self, filename: str) -> 'dict[list]':
        graph = {}
        with open(filename) as txt:
            lineCounter = 0
            lines = txt.read().split('\n')
            for i in lines:
                if lineCounter == 0:
                    self.vertices = int(i.split()[2])
                    lineCounter += 1
                    continue
                temp = i.split()
                if len(temp) != 0:
                    nodeOne = int(temp[1]) - 1
                    nodeTwo = int(temp[2]) - 1
                    if nodeOne not in graph:
                        graph[nodeOne] = [nodeTwo]
                    else:
                        graph[nodeOne].append(nodeTwo)
                    if nodeTwo not in graph:
                        graph[nodeTwo] = [nodeOne]
                    else:
                        graph[nodeTwo].append(nodeOne)
            txt.close()
        return graph

    def generate_initial_population(self, populationSize):
        # population = []
        for i in range(populationSize):
            coloring = [random.randint(0, self.numColours-1)
                        for j in range(self.vertices)]
            self.population.append(coloring)
        return self.population

    def fitness_function(self):
        self.fitness = []
        # for vertex in self.graph:
        nodeCounter = 0
        for chromosome in self.population:
            fitness = 0
            neighbourLst = self.graph[nodeCounter]
            for neighbour in neighbourLst:
                if chromosome[nodeCounter] != chromosome[neighbour]:
                    fitness += 1
            nodeCounter += 1
            if nodeCounter == 100:
                nodeCounter = 0
            self.fitness.append(fitness)
        return self.fitness

    def tournament_selection(self):
        temp = {}
        for i in range(2):
            index = random.randint(0, len(self.population)-1)
            while index in temp:
                index = random.randint(0, len(self.population)-1)
            temp[index] = self.fitness[index]
        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        for i in temp:
            return i

    def crossover(self, p1, p2):
        length = len(p1)
        offspring = [0 for i in range(length)]
        # generating random number for random set to be selected in p1
        start_range = random.randint(0, length)
        counter = 0
        while counter != length//2:
            if start_range > length-1:
                start_range = 0
            offspring[start_range] = p1[start_range]
            start_range += 1
            counter += 1
    # Now selecting the rest from p2
        temp = start_range
        while counter != length-1:
            if (start_range > length-1) or (temp > length-1):
                start_range = 0
                temp = 0
            # if p2[start_range] not in offspring:
            offspring[temp] = p2[start_range]
            counter += 1
            temp += 1
            start_range += 1
        # return offspring
        return self.mutation(offspring)

    def mutation(self, offspring):
        randomNum = random.random()
        if randomNum <= self.mutationRate:
            newIndex = random.randint(0, len(offspring)-1)
            newCol = random.randint(0, self.numColours-1)
            while offspring[newIndex] == newCol:
                newCol = random.randint(0, self.numColours-1)
            offspring[newIndex] = newCol
        return offspring

    def randomSelection(self):
        index = random.randint(0, len(self.population)-1)
        return index

    def fitnessProportional(self):
        normalizedRanges = {}
        self.fitness_function()
        totalFitness = sum(self.fitness)
        normalizedFitness = []
        for i in self.fitness:
            normalizedFitness.append(i / totalFitness)
        for i in range(len(normalizedFitness)):
            if i == 0:
                normalizedRanges[i] = normalizedFitness[i]
                continue
            normalizedRanges[i] = normalizedRanges[i-1] + normalizedFitness[i]
        randomNum = random.random()
        for i in range(len(normalizedFitness)):
            if i == 0:
                if randomNum >= 0 and randomNum < normalizedRanges[i]:
                    return i
                continue
            if randomNum >= normalizedRanges[i-1] and randomNum < normalizedRanges[i]:
                return i

    def rankBased(self):
        visited = {}
        self.fitness_function()
        maxRank = len(self.fitness)
        rankLst = [0 for i in range(maxRank)]
        tempLst = sorted(self.fitness, reverse=True)
        for i in range(len(tempLst)):
            for j in range(len(self.fitness)):
                if tempLst[i] == self.fitness[j] and j not in visited:
                    rankLst[j] = maxRank
                    maxRank -= 1
                    visited[j] = True
        normalizedRanges = {}
        normalizedRanks = []
        totalRank = sum(rankLst)
        for i in rankLst:
            normalizedRanks.append(i / totalRank)
        for i in range(len(normalizedRanks)):
            if i == 0:
                normalizedRanges[i] = normalizedRanks[i]
                continue
            normalizedRanges[i] = normalizedRanges[i-1] + normalizedRanks[i]
        randomNum = random.random()
        for i in range(len(normalizedRanks)):
            if i == 0:
                if randomNum >= 0 and randomNum < normalizedRanges[i]:
                    return i
                continue
            if randomNum >= normalizedRanges[i-1] and randomNum < normalizedRanges[i]:
                return i

    def truncation(self):
        self.fitness_function()
        temp = {}
        counter = 0
        for i in range(len(self.fitness)):
            temp[i] = self.fitness[i]
        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        tempLst = []
        for i in temp:
            if counter > self.populationSize-1:
                break
            tempLst.append(self.population[i[0]])
            counter += 1
        self.population = tempLst

    def evolve(self):
        self.population = self.generate_initial_population(self.populationSize)
        for i in range(self.generations):
            self.fitness_function()
            # p1 = self.tournament_selection()[0]
            # p2 = self.tournament_selection()[0]
            # p1 = self.fitnessProportional()
            # p2 = self.fitnessProportional()
            # p1 = self.randomSelection()
            # p2 = self.randomSelection()
            p1 = self.rankBased()
            p2 = self.rankBased()
            if p2 < p1:
                p1, p2 = p2, p1
            p1 = self.population[p1]
            p2 = self.population[p2]
            for i in range(2):
                self.population.append(self.crossover(p1, p2))
            self.truncation()
        return (self.numColours, self.fitness)


def main():
    populationSize = 10
    generationCount = 1000
    iteration = 10
    mutationProb = 0.3
    maxColours = 5
    with open("graph_col.txt", "a") as txt:
        for i in range(2, maxColours+1):
            for j in range(iteration):
                g = Graph('gcol1.txt', i, mutationProb,
                          populationSize, generationCount)
                result = g.evolve()
                print(f'numColours = {i} Fitness = {result}')

main()
# if __name__ == '__main__':
#     main()