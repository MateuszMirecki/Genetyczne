import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree
from GP.Node import Node

def calculate_fitness_function(root: Node, function_name)->int:
    input, expected_output = read_data(f"../Inputs/example_{function_name}.txt") #Zwraca input i output z pliku

    fittnesses = 0
    with open(f"../Inputs/example_{function_name}.txt", 'r') as file:
        for line_number, line_content in enumerate(file):
            number_of_test = line_number 
            interpreter = Interpreter(input_values=input[number_of_test], test=f"{root._buildTreeString()}") 
            result = interpreter.run() 
            output = result[0]
            number_or_read_input = result[4]
            input_numbers = result[3]
            new_fittness = get_fit_func(function_name)(result[0], expected_output[number_of_test], input_numbers, number_or_read_input,result[1], result[5])
    ##################################### ARGS OUT          excpected_out                  input_numbers  read_vars         current_variables     number_of_inputs_after_reading_all_vars
            fittnesses += new_fittness
        # print(fittnesses)
            
    return fittnesses



if __name__ == "__main__":
    # from collections import defaultdict
    # fitness_occurrences = defaultdict(int)
    # for i in range(400):
    #     root = generateTree(6,26)
    #     fit = calculate_fitness_function(root, "for_index")
    #     fitness_occurrences[fit] += 1

    # for fit, count in fitness_occurrences.items():
    #     print(f"Fitness {fit}: {count} occurrences")

    root = generateTree(6,6)
    root.printTree()

    fit = calculate_fitness_function(root, "1_1_A")
    print(f"fittness: {fit}")