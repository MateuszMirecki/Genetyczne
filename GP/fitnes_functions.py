import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree
from GP.Node import Node

def problem_1_1_Afitness_function(root: Node)->int:
    input, expected_output = read_data("../Inputs/example_1_1_A.txt") #Zwraca input i output z pliku

    interpreter = Interpreter(input_values=input[0], test=f"{root._buildTreeString()}") 
    result = interpreter.run() 
    output = result[0]
    number_or_read_input = result[4]
    
    new_fittness = get_fit_func("1_1_E")(result[0], expected_output[0],number_or_read_input)

    return new_fittness

tree = generateTree(5,5)
print(problem_1_1_Afitness_function(tree))