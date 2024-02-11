import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree





test = """

if ( ( ( False ) ) ) { B1 = False } read ( X4 ) read ( B3 ) read ( X5 ) write ( X5 + X4 ) if ( True ) { while ( False ) { write ( 18.64 ) read ( X1 ) } } 
"""

inf = "X1 = 16 X2 =1 while (X1 > 0) { X2 = X2 * X1 X1 = X1 - 1} "

input, output = read_data("../Inputs/example_1_2_C.txt") #Zwraca input i output z pliku

interpreter = Interpreter(input_values=input[2], test=test) 
result = interpreter.run() #Zwraca wynik testu
print("Wynik testu:")
print(f"Output {result[0]}")
print(f"Variables {result[1]}")
print(f"Counter {result[2]}")
print(f"Input_values {result[3]}")
print(f"Number of read input {result[4]}")
print(f"How many writes after reading whole input {result[5]}")
