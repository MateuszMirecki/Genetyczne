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
    interpreter = Interpreter(input_values=input[0], test=f"{root._buildTreeString()}") 
    result = interpreter.run() 
    output = result[0]
    number_or_read_input = result[4]  
    new_fittness = get_fit_func(function_name)(result[0], expected_output[0],number_or_read_input)

    return new_fittness

if __name__ == "__main__":
    root = generateTree(5,5)
    print(calculate_fitness_function(root, "1_1_A"))