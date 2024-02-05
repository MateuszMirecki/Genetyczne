import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from GP.Node import generateTree
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data

from operations import EvolutionOperations


#Populacja
population = [generateTree(9,15) for i in range(5)] #Zwraca losową populację
popolation_len = len(population)

for pop in range(popolation_len):
    print("Root after grow: " )
    print(population[pop])
    print(population[pop].printTree())
    population[pop].grow()
    print("Root after second grow: ")
    print(population[pop].printTree())
    print("=====================================")

# # LICZYMY FITNESS DLA POPULACJI
# input, expected_output = read_data("../Inputs/example_1_1_A.txt") #Zwraca input i output z pliku

# fittness = 0 #Zmienna do przechowywania fitnessu

# for inpt in range(popolation_len):
#     interpreter = Interpreter(input_values=input[inpt], test=f"{population[inpt]}") 
#     result = interpreter.run() #Zwraca wynik testu
#     output = result[0]
    
#     new_fittness = get_fit_func("1_1_A")(result[0], expected_output[inpt])
#     if new_fittness == 0:
#         print("Done")
#     else:
#         fittness += new_fittness
#     # print("Fitness: ", get_fit_func("1_1_A")(result[0]))
#     print(f"Output {result[0]} expected {expected_output[inpt]}, fitness: {fittness}")

