import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree

from operations import EvolutionOperations

population = [generateTree(4,4) for i in range(3)] #Zwraca losową populację

for pop in population:
    print(pop.printTree())

new_population = []
for i in range(0, len(population)-1):
    # print("Krzyżowanie")
    print(f" PARENT1 {population[i].printTree()} \n Parent2 {population[i+1].printTree()}")
    new_population.append(EvolutionOperations().crossover(population[i], population[i+1]))
    print(f"evoultion res {EvolutionOperations().crossover(population[i], population[i+1])}")

print ("Nowa populacja: \n\n")

for pop in new_population:
    if pop != None:
        print(pop.printTree())


