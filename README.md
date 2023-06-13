# Evolutionary Algorithm Assignment

This repository contains the implementation of an evolutionary algorithm for solving the Traveling Salesman Problem (TSP), Knapsack Problem, and Graph Coloring Problem. The algorithm uses a genetic-inspired approach to find optimal or near-optimal solutions for these combinatorial optimization problems.

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Algorithm Overview](#algorithm-overview)
- [Problem Descriptions](#problem-descriptions)
- [Results](#results)
- [Contributors](#contributors)

## Introduction
In this assignment, I have implemented an evolutionary algorithm that can solve three classic combinatorial optimization problems: TSP, Knapsack, and Graph Coloring. The evolutionary algorithm is a population-based optimization technique inspired by the principles of natural evolution, such as selection, crossover, and mutation.

The main goal of this assignment is to showcase the implementation and application of the evolutionary algorithm to solve these problems efficiently. The provided code can serve as a starting point for further experimentation and research in the field of evolutionary computation.

## Dependencies
The following dependencies are required to run the code:
- Python (version 3.x)
- NumPy
- Matplotlib (for visualizations, optional)

## Algorithm Overview
The implemented evolutionary algorithm follows these main steps:

1. **Initialization**: Generate an initial population of candidate solutions.
2. **Evaluation**: Assign fitness values to each candidate solution based on problem-specific criteria.
3. **Selection**: Select the most promising solutions from the population to proceed to the next generation.
4. **Crossover**: Combine genetic material from selected solutions to produce offspring.
5. **Mutation**: Introduce random changes to the offspring to explore new regions of the solution space.
6. **Replacement**: Replace some solutions in the population with the new offspring.
7. Repeat steps 2-6 until a termination criterion is met (e.g., a maximum number of generations or a satisfactory solution is found).

The algorithm iterates through these steps, gradually improving the quality of the solutions in the population over generations.

## Problem Descriptions
### Traveling Salesman Problem (TSP)
The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits all given cities and returns to the starting city. The algorithm attempts to find an optimal permutation of cities that minimizes the total distance traveled.

### Knapsack Problem
The Knapsack Problem involves selecting a subset of items from a given set, each with its own weight and value, to maximize the total value while keeping the total weight within a given limit. The algorithm aims to find the best combination of items that maximizes the total value.

### Graph Coloring Problem
The Graph Coloring Problem requires assigning colors to the vertices of a graph such that no two adjacent vertices share the same color. The algorithm seeks to find a valid coloring with the minimum number of colors.

## Results
The repository includes example results and visualizations obtained by running the evolutionary algorithm on the provided problem instances.

## Contributors
This was a group assignment completed in collaboration with [Muhammad Murtaza]( https://github.com/mm06369/ ).

<a href="https://github.com/aliasgharchakera/CI-Spring23-Assignment01/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aliasgharchakera/CI-Spring23-Assignment01" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
