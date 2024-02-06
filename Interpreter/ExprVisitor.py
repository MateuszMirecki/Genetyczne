from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

class ExprVisitor(ParseTreeVisitor):

    def __init__(self, input_values=[4,5,6], instruction_limit=100000, output_limit=100, max_loop_iterations=1000):
        self.variables = {}
        self.output = []
        self.output_limit = output_limit
        self.input_values = input_values
        self.input_index = -1
        self.instruction_limit = instruction_limit
        self.counter = 0
        self.loop_iterations = 0
        self.max_loop_iterations = max_loop_iterations
        self.number_of_read_numeric_var = 0
        
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        with open('output.txt', 'w') as f:
            f.write(str(ctx.getText()))
        for expression in ctx.expressions():
            if self.counter >= self.instruction_limit:
                return [self.output, self.variables, self.counter]
            self.visitChildren(expression)
        return [self.output, self.variables, self.counter]
        

    def visitExpressions(self, ctx:ExprParser.ExpressionsContext):

        # Increment the counter only when an actual expression is evaluated
        if ctx.getText() not in ['{', '}']:
            self.counter += 1
            if self.counter > self.instruction_limit:
                # print ("Instruction limit reached.")
                return 0

        result = self.visitChildren(ctx)
        return result


    def visitIf_statement(self, ctx:ExprParser.If_statementContext):
        self.counter += 1
        if ctx.getChild(2).getText() == 'True':
            return self.visitBlock_statement(ctx.getChild(4))
        

    def visitWhile_loop(self, ctx:ExprParser.While_loopContext):
        self.counter += 1
        if self.loop_iterations > self.max_loop_iterations:
            # print ("Max loop iterations reached.")
            return
        # print(self.loop_iterations)
        # print(self.counter)
        # print(ctx.getText())
        while True:
            condition = self.visitBool_value(ctx.bool_value())
            # print(condition)
            if self.counter > self.instruction_limit:
                print ("Instruction limit reached.")
                return 0
            if condition:
                if self.loop_iterations > self.max_loop_iterations:
                    # print ("Max loop iterations reached.")
                    return
                self.loop_iterations += 1

                self.visitBlock_statement(ctx.block_statement())
            else:
                break


        


    def visitBlock_statement(self, ctx):
        self.counter += 1
        if ctx:
            # Skip the first and last child as they are LEFTBRACK and RIGHTBRACK
            for i in range(1, ctx.getChildCount() - 1):
                
                child = ctx.getChild(i)
                
                self.visit(child)



    def visitWrite_val(self, ctx:ExprParser.Write_valContext):
        self.counter += 1

        expression = ctx.getChild(2)
        if self.isBooleanExpression(expression):
            bool_val = (self.visitBool_value(expression))
            if bool_val:
                self.output.append(1)
            else:
                self.output.append(0)
        else:
            self.output.append(self.visitNumeric_value(expression))
        
    

    def visitRead_var(self, ctx:ExprParser.Read_varContext):
        self.counter += 1

        variable_name = ctx.getText()
        if variable_name:
            variable_name = ctx.getChild(2).getText()
            if variable_name[0] == 'X':
                self.number_of_read_numeric_var += 1

                self.incrementInputIndex()
                if self.input_values[self.input_index] == 'True':
                    self.variables[variable_name] = 1
                elif self.input_values[self.input_index] == 'False':
                    self.variables[variable_name] = 0
                else:
                    self.variables[variable_name] = int(self.input_values[self.input_index])
            elif variable_name[0] == 'B':
                self.incrementInputIndex()
                if self.input_values[self.input_index] == 'True' or self.input_values[self.input_index] == 'False':
                    self.variables[variable_name] = self.input_values[self.input_index]
                else:
                    if int(self.input_values[self.input_index]) == 0:
                        self.variables[variable_name] = 'False'
                    else:
                        self.variables[variable_name] = 'True'
        else:
            print("Wrong variable name in read_var - skipping") 
            pass


    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        self.counter += 1

        variable_name = ctx.getChild(0).getText()
        value_expression = ctx.getChild(2)
        if value_expression is None:
            return 


        # Handling assignment to boolean variables
        elif variable_name.startswith('B'):
            # Evaluate the boolean expression
            bool_value = self.visitBool_value(value_expression)
            self.variables[variable_name] = bool_value
            return bool_value

        # Handling assignment to numeric variables
        elif variable_name.startswith('X'):
            numeric_value = self.visitNumeric_value(value_expression)
            self.variables[variable_name] = numeric_value
            return numeric_value
        
        if value_expression.getText() in ['True', 'False']:
            bool_value = value_expression.getText() == 'True'

            # Assign 1 for True and 0 for False to both boolean and numeric variables
            assigned_value = 1 if bool_value else 0
            self.variables[variable_name] = assigned_value
            return assigned_value

        else:
            raise Exception("Unrecognized assignment type")




    def visitBool_value(self, ctx:ExprParser.Bool_valueContext):
        self.counter += 1

        if ctx.TRUE() is not None:
            return True
        elif ctx.FALSE() is not None:
            return False

        elif ctx.BOOL_VAR() is not None:
            if ctx.BOOL_VAR().getText() in self.variables:
                value_of_bool = self.variables[ctx.BOOL_VAR().getText()]
                return (value_of_bool)
            else:
                return False

        elif ctx.NOT() is not None:
            return not self.visitBool_value(ctx.bool_value(0))

        elif ctx.LEFTPREN() is not None and ctx.RIGHTPREN() is not None:
            return self.visitBool_value(ctx.bool_value(0))

        elif ctx.AND() is not None or ctx.OR() is not None:
            left_bool = self.visitBool_value(ctx.bool_value(0))
            right_bool = self.visitBool_value(ctx.bool_value(1))
            if ctx.AND() is not None:
                return left_bool and right_bool
            elif ctx.OR() is not None:
                return left_bool or right_bool

       # Condition for a single numeric value
        elif ctx.getChildCount() == 1 and ctx.numeric_value() is not None:
            numeric_value = self.visitNumeric_value(ctx.numeric_value(0))
            return numeric_value != 0  # True for non-zero, False for zero

        # Condition for comparison between two numeric values
        elif ctx.numeric_value(0) is not None and ctx.numeric_value(1) is not None:
            left = self.visitNumeric_value(ctx.numeric_value(0))
            right = self.visitNumeric_value(ctx.numeric_value(1))


            if ctx.EQ() is not None:
                return left == right
            elif ctx.NEQ() is not None:
                return left != right
            elif ctx.LE() is not None:
                return left < right
            elif ctx.LEQ() is not None:
                return left <= right
            elif ctx.GE() is not None:
                return left > right
            elif ctx.GEQ() is not None:
                return left >= right
            else:
                raise Exception("Invalid comparison operation in boolean expression")

        else:
            raise Exception("Unrecognized boolean expression")

        
    def visitNumeric_value(self, ctx:ExprParser.Numeric_valueContext):
        self.counter += 1
        if ctx is None:
            return 0

        # Check for expression within parentheses
        if ctx.LEFTPREN() is not None and ctx.RIGHTPREN() is not None:
            return self.visitNumeric_value(ctx.numeric_value(0))

        # Unary negation
        if ctx.SUB() is not None and ctx.getChildCount() == 2:
            negation_value = self.visitNumeric_value(ctx.numeric_value(0))
            if negation_value is None:
                #print
                return None
            return -negation_value

        # Binary operations
        if ctx.getChildCount() == 3:
            left_ctx = ctx.numeric_value(0)
            right_ctx = ctx.numeric_value(1)

            if left_ctx is None or right_ctx is None:
                return None

            left = self.visitNumeric_value(left_ctx)
            right = self.visitNumeric_value(right_ctx)

            if left is None or right is None:
                return None

            if ctx.MUL() is not None:
                return left * right
            elif ctx.DIV() is not None:
                # Check for division by zero or a very small number
                if right == 0 or abs(right) < 1/1000:
                    return 1  # Return 1 for division by zero or by a very small number
                else:
                    return left // right
            elif ctx.ADD() is not None:
                return left + right
            elif ctx.SUB() is not None:
                return left - right

        # Check for NUMBER
        if ctx.NUMBER() is not None:
            return int(ctx.NUMBER().getText())

        # Check for NUM_VAR
        elif ctx.NUM_VAR() is not None:
            var_name = ctx.NUM_VAR().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                self.variables[var_name] = 0
                return 0

        else:
            raise Exception("Unrecognized numeric expression")


#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
########## UTILS FUNCTIONS ############
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################

        
    def incrementInputIndex(self):
        if self.input_index < len(self.input_values)- 1:
            self.input_index += 1
        else:  
            self.input_index = -1
        
    def isBooleanExpression(self, expression):
        if expression.getText() in ["True", "False"]:
            return True

        if expression.getChildCount() == 1 and isinstance(expression.getChild(0), TerminalNode):
            childText = expression.getChild(0).getText()
            if childText.startswith('B') and childText[1:].isdigit():
                return True

        text = expression.getText()

        if text.startswith('!'):
            return self.isBooleanExpression(expression.getChild(1))

        if '&&' in text or '||' in text:
            return all(self.isBooleanExpression(expression.getChild(i)) for i in range(expression.getChildCount()) if i % 2 == 0)

        if any(op in text for op in ["==", "!=", "<", "<=", ">", ">="]):
            return True

        if text.startswith('(') and text.endswith(')'):
            innerExpression = self.getInnerExpression(expression)
            return self.isBooleanExpression(innerExpression)

        return False
    


    def getInnerExpression(self, expression):
        """
        Recursively removes the outermost parentheses and returns the inner expression.
        """
        text = expression.getText()
        if text.startswith('(') and text.endswith(')'):
            # Remove the outermost parentheses and get the new expression
            # This could be adapted based on how your parse tree is structured
            return self.getInnerExpression(expression.getChild(1))
        else:
            return expression





del ExprParser