from Node import generateTree
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data

from operations import EvolutionOperations



##### MUTACJA #####

# population = [generateTree() for i in range(5)] #Zwraca losową populację

# for pop in population:
#     print(pop.printTree())

# new_population = []
# for root in population:
#     # print("Mutacja")
#     new_population.append(EvolutionOperations().mutation(root))
    
# for pop in new_population:
#     print(pop)
#     if pop != None:
#         print(pop.printTree())

#### KONIEC MUTACJI ####

#####################################################################

#### KRZYŻOWANIE  DO ZROBIENIA ####

# population = [generateTree() for i in range(3)] #Zwraca losową populację

# for pop in population:
#     print(pop.printTree())

# new_population = []
# for i in range(0, len(population)-1):
#     # print("Krzyżowanie")
#     print(f" PARENT1 {population[i].printTree()} \n Parent2 {population[i+1].printTree()}")
#     new_population.append(EvolutionOperations().crossover(population[i], population[i+1]))
#     print(f"evoultion res {EvolutionOperations().crossover(population[i], population[i+1])}")

# print ("Nowa populacja: \n\n")

# for pop in new_population:
#     if pop != None:
#         print(pop.printTree())

#### KONIEC KRZYŻOWANIA ####


#####################################################################


### POCZAĄTEK TESTÓW JEDNEGO TESTOW###

# ROBIY POPULACJE
population = [generateTree() for i in range(5)] #Zwraca losową populację
popolation_len = len(population)

## LICZYMY FITNESS DLA POPULACJI
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


#### KONIEC TESTÓW JEDNEGO TESTU ####
    


#####################################################################


### TEST INTERPRETERA ###

# tree = generateTree() #Zwraca losowe drzewo
# input, output = read_data("../Inputs/example_1_1_A.txt") #Zwraca input i output z pliku
# # print(input, output)

# test = "X1 = 6 X2 = 1 while(X1>0){X2 = X2*X1 X1 = X1-1} write(X2)"
# inf = "while (X1 > -5) { X2 = 2}"

# interpreter = Interpreter(input_values=[1,2,3], test=test) 
# result = interpreter.run() #Zwraca wynik testu
# print("Wynik testu:")
# print(f"Output {result[0]}")
# print(f"Variables {result[1]}")
# print(f"Counter {result[2]}")
# print(f"Input_values {result[3]}")
