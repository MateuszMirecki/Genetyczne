from Interpreter.ExprVisitor import ExprVisitor
from Interpreter.ExprParser import ExprParser
from Interpreter.ExprLexer import ExprLexer
from antlr4 import *
import csv

class Interpreter:
    def __init__(self, input_values=None,test="B1 = True X2 = 2"):
        if input_values is None:
            input_values = []
        self.input_values = input_values
        self.test = test

    def run(self):
        lexer = ExprLexer(InputStream(self.test))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.program()
        visitor = ExprVisitor(self.input_values)
        visitor.visit(tree)
        return visitor.output, visitor.variables, visitor.counter, visitor.input_values, visitor.number_of_read_numeric_var

# Usage example
# interpreter = Interpreter()

# values = []
# with open('../Inputs/input.txt', 'r') as file:
#     for line in file:
#         line_values = [val.strip() for val in line.split()]
#         values.extend(line_values)

# interpreter.input_values = values

# make_it_pass = "B1 = True X2 = 2"
# print(f"Test: " + make_it_pass)
# result = interpreter.run(test=make_it_pass)
# print("Wynik testu:")
# print(result)

# Uncomment to run additional tests
# for test in tests:
#     print("\n\n\n")
#     print(f"Test: " + test)
#     result = interpreter.run(test=test)
#     print("Wynik testu:")
#     print(result)
#     print("\n\n\n")
