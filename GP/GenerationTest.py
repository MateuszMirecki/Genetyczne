import sys
import os
import random
import copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import Node, generateTree
from operations import EvolutionOperations, Run, Program



if __name__ == "__main__":
    inputs, expected_outputs = read_data("../Inputs/example_1_1_E.txt")
    fitness_function = get_fit_func("1_1_E")

    gp_run = Run(population_size=1000, fitness_function=fitness_function, depth=5, max_width=5, inputs=inputs, expected_outputs=expected_outputs)
    gp_run.run()