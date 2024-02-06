import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree

from operations import EvolutionOperations

# ROBIY POPULACJE
population = [generateTree(5,5) for i in range(1000)] #Zwraca losową populację
popolation_len = len(population)

# LICZYMY FITNESS DLA POPULACJI
input, expected_output = read_data("../Inputs/example_1_1_E.txt") #Zwraca input i output z pliku

fittness = 0 #Zmienna do przechowywania fitnessu

for population_index in range(popolation_len):
    input_index = population_index % len(input)
    output_index = population_index % len(expected_output)

    interpreter = Interpreter(input_values=input[input_index], test=f"{population[population_index]._buildTreeString()}") 
    result = interpreter.run() 
    output = result[0]
    number_or_read_input = result[4]
    
    new_fittness = get_fit_func("1_1_E")(result[0], expected_output[output_index],number_or_read_input)
    if new_fittness == 0:
        with open('pass.txt', 'w') as file:
            file.write(f"Program passed\n{population[population_index]._buildTreeString()}\n")
            file.write(f"output {result[0]}\n")
        
    else:
        fittness += new_fittness



    

