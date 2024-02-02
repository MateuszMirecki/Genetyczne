# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
# if "." in __name__:
#     from .ExprParser import ExprParser
# else:
#     from ExprParser import ExprParser

from Interpreter.ExprVisitor import ExprVisitor
from Interpreter.ExprParser import ExprParser
from Interpreter.ExprLexer import ExprLexer
from GP.NodeType import NodeType
from GP.Node import Node

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    def __init__(self):
        self.current_node: Node = None


    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        self.current_node = Node(NodeType.program)

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#expressions.
    def enterExpressions(self, ctx:ExprParser.ExpressionsContext):
        expression_node = Node(NodeType.expressions, parent=self.current_node)
        self.current_node.children.append(expression_node)
        self.current_node = expression_node

    # Exit a parse tree produced by ExprParser#expressions.
    def exitExpressions(self, ctx:ExprParser.ExpressionsContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#while_loop.
    def enterWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#while_loop.
    def exitWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#block_statement.
    def enterBlock_statement(self, ctx:ExprParser.Block_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#block_statement.
    def exitBlock_statement(self, ctx:ExprParser.Block_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#write_val.
    def enterWrite_val(self, ctx:ExprParser.Write_valContext):
        pass

    # Exit a parse tree produced by ExprParser#write_val.
    def exitWrite_val(self, ctx:ExprParser.Write_valContext):
        pass


    # Enter a parse tree produced by ExprParser#read_var.
    def enterRead_var(self, ctx:ExprParser.Read_varContext):
        pass

    # Exit a parse tree produced by ExprParser#read_var.
    def exitRead_var(self, ctx:ExprParser.Read_varContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        print(ctx.getText())

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#bool_value.
    def enterBool_value(self, ctx:ExprParser.Bool_valueContext):
        print(ctx.getText())

    # Exit a parse tree produced by ExprParser#bool_value.
    def exitBool_value(self, ctx:ExprParser.Bool_valueContext):
        pass


    # Enter a parse tree produced by ExprParser#numeric_value.
    def enterNumeric_value(self, ctx:ExprParser.Numeric_valueContext):
        pass

    # Exit a parse tree produced by ExprParser#numeric_value.
    def exitNumeric_value(self, ctx:ExprParser.Numeric_valueContext):
        print(ctx.getText())



# del ExprParser

if __name__ == "__main__":
    test = "X1 = 6 X2 = 1 while(X1>0){X2 = X2*X1 X1 = X1-1} write(X2)"
    test2 = "X1 = 6"

    lexer = ExprLexer(InputStream(test2))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    listener = ExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
