import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree

from operations import EvolutionOperations


# interpreter = Interpreter(input_values=input[0], test=f"{population[0]._buildTreeString()}") 
# result = interpreter.run() #Zwraca wynik testu
# print(result)

# ROBIY POPULACJE
population = [generateTree(6,6) for i in range(10000)] #Zwraca losową populację
popolation_len = len(population)

# LICZYMY FITNESS DLA POPULACJI
input, expected_output = read_data("../Inputs/example_1_2_A.txt") #Zwraca input i output z pliku

fittness = 0 #Zmienna do przechowywania fitnessu


for population_index in range(popolation_len):
    input_index = population_index % len(input)
    output_index = population_index % len(expected_output)

    interpreter = Interpreter(input_values=input[input_index], test=f"{population[population_index]._buildTreeString()}") 
    result = interpreter.run() 
    output = result[0]
    number_or_read_input = result[4]
    
    new_fittness = get_fit_func("1_2_A")(result[0], expected_output[output_index],number_or_read_input)
    if new_fittness == 0:
        # Open a file named 'output.txt' in write mode
        with open('pass.txt', 'w') as file:
            # Assuming population, population_index, and result are defined previously
            # Write the first output line
            file.write(f"Program passed\n{population[population_index]._buildTreeString()}\n")
            # Write the second output line
            file.write(f"output {result[0]}\n")
            # Write "Done"
            file.write("Done\n")

        
    else:
        fittness += new_fittness
    # print("Fitness: ", get_fit_func("1_1_A")(result[0]))
    # print(f"Output {result[0]} expected {expected_output[output_index]}, fitness: {fittness}")


    

