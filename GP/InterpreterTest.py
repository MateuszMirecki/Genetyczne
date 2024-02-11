import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Interpreter.run_interpreter import Interpreter
from fitness_functions import get_fit_func
from read_data import read_data
from GP.Node import generateTree





test = """

read ( X4 ) B3 = 54.49 * 95.34 > X1 read ( X1 ) X5 = 5.32 + 24.96 * X2 - X3 while ( 77.18 / 87.87 != 34.63 + 13.11 ) { if ( False ) { read ( X4 ) } if ( False ) { } read ( X5 ) } write ( X1 )

"""

inf = "X1 = 16 X2 =1 while (X1 > 0) { X2 = X2 * X1 X1 = X1 - 1} "

input, output = read_data("../Inputs/example_26_median.txt") #Zwraca input i output z pliku

interpreter = Interpreter(input_values=input[2], test=test) 
result = interpreter.run() #Zwraca wynik testu
print("Wynik testu:")
print(f"Output {result[0]}")
print(f"Variables {result[1]}")
print(f"Counter {result[2]}")
print(f"Input_values {result[3]}")
print(f"Number of read input {result[4]}")
print(f"How many writes after reading whole input {result[5]}")
