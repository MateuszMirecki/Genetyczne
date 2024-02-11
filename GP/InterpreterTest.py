import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree





test = """

while ( B2 ) { X5 = 81.68 write ( 70.87 ) } write ( 39.18 - 53.99 ) 

"""

inf = "X1 = 16 X2 =1 while (X1 > 0) { X2 = X2 * X1 X1 = X1 - 1} "

input, output = read_data("../Inputs/example_1_1_A.txt") #Zwraca input i output z pliku

interpreter = Interpreter(input_values=input[2], test=test) 
result = interpreter.run() #Zwraca wynik testu
print("Wynik testu:")
print(f"Output {result[0]}")
print(f"Variables {result[1]}")
print(f"Counter {result[2]}")
print(f"Input_values {result[3]}")
print(f"Number of read input {result[4]}")
print(f"How many writes after reading whole input {result[5]}")
