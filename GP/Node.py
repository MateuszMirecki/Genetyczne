from typing import Any
from NodeType import NodeType
import random

MAX_NUMBER_OF_GENERATED_EXPRESSIONS = 1
MAX_EXPRESSIONS_IN_TREE = 1
MAX_FUNCTION_DIMENSION = 1
MAX_BOOL_VAR_DIMENSION = 1



class Node:
    def __init__(self,
                 node_type: NodeType = None,
                 value: str | None = None,
                 isterminal: bool = False,
                 parent = None,
                 embedded_expressions = 0
                 ):
        self.node_type = node_type
        self.value = value
        self.children = []
        self.parent = parent
        self.isterminal = isterminal
        self.embedded_expressions = embedded_expressions

    def __str__(self):
        if self.isterminal:
            str = self.value
        else:
            str = ""
        for child in self.children:
            str += child.__str__()
        return str

    def printTree(self) -> str:
        return self._buildTreeString()

    def _buildTreeString(self) -> str:
        tree_str = ""
        for child in self.children:
            if child.isterminal:
                tree_str += child.value + " "
            else:
                tree_str += child._buildTreeString()
        return tree_str

    def grow(self) -> None:
        match self.node_type:
            case NodeType.program:
                self.children.append(Node(NodeType.expressions,parent=self))

            case NodeType.expressions:
                choiceList = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment]
                chosen_element = random.choice(choiceList)
                self.children.append(Node(chosen_element, parent=self, embedded_expressions=self.embedded_expressions))

                if self.embedded_expressions < MAX_EXPRESSIONS_IN_TREE:
                    number_of_expressions = random.randint(1, MAX_NUMBER_OF_GENERATED_EXPRESSIONS)

                    for i in range(number_of_expressions):
                        self.children.append(Node(NodeType.expressions, parent=self, embedded_expressions=self.embedded_expressions+1))


            case NodeType.if_statement:
                self.children.append(Node(NodeType.IF,value = "if",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                self.children.append(Node(NodeType.bool_value,parent=self))
                self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTBRACK, value = "{",parent=self, isterminal=True))
                if self.embedded_expressions < MAX_EXPRESSIONS_IN_TREE:
                    self.children.append(Node(NodeType.expressions,parent=self, embedded_expressions=self.embedded_expressions+1))
                self.children.append(Node(NodeType.RIGHTBRACK, value = "}",parent=self, isterminal=True))


            case NodeType.while_loop:
                self.children.append(Node(NodeType.WHILE, value = "while",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                self.children.append(Node(NodeType.bool_value, parent=self))
                self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTBRACK, value = "{",parent=self, isterminal=True))
                if self.embedded_expressions < MAX_EXPRESSIONS_IN_TREE:
                    self.children.append(Node(NodeType.expressions,parent=self, embedded_expressions=self.embedded_expressions+1))

                self.children.append(Node(NodeType.RIGHTBRACK, value = "}", parent=self, isterminal=True))


            case NodeType.wrtie_val:
                choiceList = [NodeType.numeric_value, NodeType.bool_value]
                chosen_element = random.choice(choiceList)

                self.children.append(Node(NodeType.WRITE, value = "write",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                self.children.append(Node(chosen_element,parent=self))
                self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))


            case NodeType.read_var:
                choiceList = [NodeType.NUM_VAR, NodeType.BOOL_VAR]
                chosen_element = random.choice(choiceList)

                self.children.append(Node(NodeType.READ, value = "read",parent=self, isterminal=True))
                self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                match chosen_element:
                    case NodeType.NUM_VAR:
                        self.children.append(Node(NodeType.NUM_VAR, value = "X"+str(random.randint(1, MAX_FUNCTION_DIMENSION)),parent=self, isterminal=True))
                    case NodeType.BOOL_VAR:
                        self.children.append(Node(NodeType.BOOL_VAR, value = "B"+str(random.randint(1, MAX_BOOL_VAR_DIMENSION)),parent=self, isterminal=True))
                self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))

            case NodeType.assignment:
                choiceList = [NodeType.numeric_value, NodeType.bool_value]
                chosen_element = random.choice(choiceList)
                if chosen_element == NodeType.numeric_value:
                    variable_number = str(random.randint(1, MAX_FUNCTION_DIMENSION))
                    self.children.append(Node(NodeType.NUM_VAR, value = "X"+variable_number ,parent=self, isterminal=True))
                else:
                    variable_number = str(random.randint(1, MAX_BOOL_VAR_DIMENSION))
                    self.children.append(Node(NodeType.BOOL_VAR, value = "B"+variable_number ,parent=self, isterminal=True))
                self.children.append(Node(NodeType.EQ, value = "=",parent=self, isterminal=True))
                self.children.append(Node(chosen_element,parent=self))

            case NodeType.bool_value:
                option = random.randint(1,6)
                match option:
                    case 1:
                        choiceList = [NodeType.TRUE, NodeType.FALSE]
                        chosen_element = random.choice(choiceList)
                        if chosen_element == NodeType.TRUE:
                            self.children.append(Node(NodeType.TRUE, value = "True",parent=self, isterminal=True))
                        else:
                            self.children.append(Node(NodeType.FALSE, value = "False",parent=self, isterminal=True))
                    case 2:
                        self.children.append(Node(NodeType.BOOL_VAR, value = "B"+str(random.randint(1, MAX_BOOL_VAR_DIMENSION)),parent=self, isterminal=True))
                    case 3:
                        self.children.append(Node(NodeType.NOT, value = "!",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.bool_value,parent=self))
                    case 4:
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                        choiceList = [NodeType.EQ, NodeType.NEQ, NodeType.LE, NodeType.LEQ, NodeType.GE, NodeType.GEQ]
                        chosen_element = random.choice(choiceList)
                        match chosen_element:
                            case NodeType.EQ:
                                self.children.append(Node(NodeType.EQ, value = "==",parent=self, isterminal=True))
                            case NodeType.NEQ:
                                self.children.append(Node(NodeType.NEQ, value = "!=",parent=self, isterminal=True))
                            case NodeType.LE:
                                self.children.append(Node(NodeType.LE, value = "<",parent=self, isterminal=True))
                            case NodeType.LEQ:
                                self.children.append(Node(NodeType.LEQ, value = "<=",parent=self, isterminal=True))
                            case NodeType.GE:
                                self.children.append(Node(NodeType.GE, value = ">",parent=self, isterminal=True))
                            case NodeType.GEQ:
                                self.children.append(Node(NodeType.GEQ, value = ">=",parent=self, isterminal=True))
                            case _:
                                print("Error1")
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                    case 5:
                        self.children.append(Node(NodeType.bool_value,parent=self))
                        choiceList = [NodeType.AND, NodeType.OR]
                        chosen_element = random.choice(choiceList)
                        match chosen_element:
                            case NodeType.AND:
                                self.children.append(Node(NodeType.AND, value = "&&",parent=self, isterminal=True))
                            case NodeType.OR:
                                self.children.append(Node(NodeType.OR, value = "||",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.bool_value,parent=self))
                    case 6:
                        self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.bool_value,parent=self))
                        self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))
                    case _:
                        print("Error2")
            case NodeType.numeric_value:
                option = random.randint(1, 5)
                match option:
                    case 1:
                        self.children.append(Node(NodeType.NUMBER, value = str(random.randint(1, 1000)),parent=self, isterminal=True))
                    case 2:
                        self.children.append(Node(NodeType.NUM_VAR, value = "X"+str(random.randint(1, MAX_FUNCTION_DIMENSION)),parent=self, isterminal=True))
                    case 3:
                        self.children.append(Node(NodeType.SUB, value = "-",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                    case 4:
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                        choiceList = [NodeType.ADD, NodeType.SUB, NodeType.MUL, NodeType.DIV]
                        chosen_element = random.choice(choiceList)
                        match chosen_element:
                            case NodeType.ADD:
                                self.children.append(Node(NodeType.ADD, value = "+",parent=self, isterminal=True))
                            case NodeType.SUB:
                                self.children.append(Node(NodeType.SUB, value = "-",parent=self, isterminal=True))
                            case NodeType.MUL:
                                self.children.append(Node(NodeType.MUL, value = "*",parent=self, isterminal=True))
                            case NodeType.DIV:
                                self.children.append(Node(NodeType.DIV, value = "/",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                    case 5:
                        self.children.append(Node(NodeType.LEFTPREN, value = "(",parent=self, isterminal=True))
                        self.children.append(Node(NodeType.numeric_value,parent=self))
                        self.children.append(Node(NodeType.RIGHTPREN, value = ")",parent=self, isterminal=True))
                    case _:
                        print("Error3")
            # case NodeType.terminal:
            #     return

        self.growChildren()


    def growChildren(self):
        for child in self.children:
            if not child.isterminal:
                child.grow()


def generateTree():
    root = Node(NodeType.program)
    root.grow()
    return root

if __name__ == "__main__":
    generateTree()