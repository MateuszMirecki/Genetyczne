import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree

from operations import EvolutionOperations



##### MUTACJA #####

population = [generateTree() for i in range(5)] #Zwraca losową populację

for pop in population:
    print(pop.printTree())

new_population = []
for root in population:
    # print("Mutacja")
    new_population.append(EvolutionOperations().mutation(root))
    
for pop in new_population:
    print(pop)
    if pop != None:
        print(pop.printTree())

#### KONIEC MUTACJI ####