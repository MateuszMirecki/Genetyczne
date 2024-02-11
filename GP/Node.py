import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from typing import Any
from GP.NodeType import NodeType
import random

MIN_NUMERIC = 0
MAX_NUMERIC = 100



MAX_FUNCTION_DIMENSION = 5
MAX_BOOL_VAR_DIMENSION = 3

class Node:
    def __init__(self,
                 node_type: NodeType = None,
                 value: str | None = None,
                 isterminal: bool = False,
                 parent=None,   
                 depth=10,
                 max_width=2,
                 ):
        self.node_type = node_type
        self.value = value
        self.children = []
        self.parent = parent
        self.isterminal = isterminal
        self.depth = depth
        self.max_width = max_width

    def __str__(self):
        return f"Node type: {self.node_type}, Value: {self.value}, Terminal: {self.isterminal}, Depth: {self.depth}"

    def printTree(self) -> str:
        print(self._buildTreeString())

    def _buildTreeString(self) -> str:
        tree_str = ""
        for child in self.children:
            if child.isterminal:
                tree_str += child.value + " "
            else:
                tree_str += child._buildTreeString()
        return tree_str

    def grow_program(self):
        for _ in range(random.randint(1, self.max_width)):
            self.children.append(Node(NodeType.expressions, parent=self, depth=self.depth - 1, max_width=self.max_width))

    def grow_expressions(self):
        choiceList = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                      NodeType.read_var, NodeType.assignment]

        chosen_expression_type = random.choice(choiceList)
        if self.children == []:
            self.children.append(Node(chosen_expression_type, parent=self, depth=self.depth - 1, max_width=self.max_width))

    def grow_if_statement(self):
        current_depth = self.depth

        # if statement
        self.children.append(Node(NodeType.IF, value="if", parent=self, isterminal=True, depth=current_depth - 1,max_width=self.max_width))
        self.children.append(Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=current_depth - 1,max_width=self.max_width))
        self.children.append(Node(NodeType.bool_value, parent=self, depth=current_depth - 1,max_width=self.max_width))
        self.children.append(Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=current_depth - 1,max_width=self.max_width))

        # blck statement
        self.children.append(Node(NodeType.LEFTBRACK, value="{", parent=self, isterminal=True, depth=current_depth - 1, max_width=self.max_width))
        # borders width of tree
       
        self.children.append(Node(NodeType.expressions, parent=self, depth=current_depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.RIGHTBRACK, value="}", parent=self, isterminal=True, depth=current_depth - 1, max_width=self.max_width))

    def grow_while_loop(self):
        self.children.append(Node(NodeType.WHILE, value="while", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.bool_value, parent=self, depth=self.depth - 1))
        self.children.append(Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))


        self.children.append(Node(NodeType.LEFTBRACK, value="{", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
        for _ in range(random.randint(0, self.max_width)):
            self.children.append(Node(NodeType.expressions, parent=self, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.RIGHTBRACK, value="}", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))

    def grow_write_val(self):
        
        # choiceList = [NodeType.numeric_value, NodeType.bool_value]
        # chosen_element = random.choice(choiceList)

        if random.random() < 0.99:
            chosen_element = NodeType.numeric_value
        else:
            chosen_element = NodeType.bool_value

        self.children.append(Node(NodeType.WRITE, value="write", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(chosen_element, parent=self, depth=self.depth - 1, max_width=self.max_width))
        self.children.append(Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))

    def grow_read_var(self):

        if random.random() < 0.95:
            chosen_element = NodeType.NUM_VAR
        else:
            chosen_element = NodeType.BOOL_VAR

        if self.children == []:
            self.children.append(Node(NodeType.READ, value="read", parent=self, isterminal=True, depth=self.depth - 1))
            self.children.append(Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=self.depth - 1))
            match chosen_element:
                case NodeType.NUM_VAR:
                    self.children.append(
                        Node(NodeType.NUM_VAR, value="X" + str(random.randint(1, MAX_FUNCTION_DIMENSION)), parent=self,
                            isterminal=True, depth=self.depth - 1))
                case NodeType.BOOL_VAR:
                    self.children.append(
                        Node(NodeType.BOOL_VAR, value="B" + str(random.randint(1, MAX_BOOL_VAR_DIMENSION)), parent=self,
                            isterminal=True, depth=self.depth - 1, max_width=self.max_width))
            self.children.append(Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))

    def grow_assignment(self):
        choiceList = [NodeType.numeric_value, NodeType.bool_value]
        chosen_element = random.choice(choiceList)
        if self.children == []:
            if chosen_element == NodeType.numeric_value:
                variable_number = str(random.randint(1, MAX_FUNCTION_DIMENSION))
                self.children.append(
                    Node(NodeType.NUM_VAR, value="X" + variable_number, parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
            else:
                variable_number = str(random.randint(1, MAX_BOOL_VAR_DIMENSION))
                self.children.append(Node(NodeType.BOOL_VAR, value="B" + variable_number, parent=self, isterminal=True,
                                        depth=self.depth - 1, max_width=self.max_width))
            self.children.append(Node(NodeType.EQ, value="=", parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
            self.children.append(Node(chosen_element, parent=self, depth=self.depth - 1, max_width=self.max_width))

    def grow_bool_value(self):
        option = random.randint(1, 6)
        if self.children == []:
            match option:
                case 1:
                    choiceList = [NodeType.TRUE, NodeType.FALSE]
                    chosen_element = random.choice(choiceList)
                    if chosen_element == NodeType.TRUE:
                        self.children.append(
                            Node(NodeType.TRUE, value="True", parent=self, isterminal=True, depth=self.depth - 1,
                                max_width=self.max_width))
                    else:
                        self.children.append(
                            Node(NodeType.FALSE, value="False", parent=self, isterminal=True, depth=self.depth - 1,
                                max_width=self.max_width))
                case 2:
                    self.children.append(
                        Node(NodeType.BOOL_VAR, value="B" + str(random.randint(1, MAX_BOOL_VAR_DIMENSION)), parent=self,
                            isterminal=True, depth=self.depth - 1, max_width=self.max_width))
                case 3:
                    self.children.append(Node(NodeType.NOT, value="!", parent=self, isterminal=True, depth=self.depth - 1,
                                            max_width=self.max_width))
                    self.children.append(Node(NodeType.bool_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                case 4:
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                    choiceList = [NodeType.EQ, NodeType.NEQ, NodeType.LE, NodeType.LEQ, NodeType.GE, NodeType.GEQ]
                    chosen_element = random.choice(choiceList)
                    match chosen_element:
                        case NodeType.EQ:
                            self.children.append(
                                Node(NodeType.EQ, value="==", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.NEQ:
                            self.children.append(
                                Node(NodeType.NEQ, value="!=", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.LE:
                            self.children.append(
                                Node(NodeType.LE, value="<", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.LEQ:
                            self.children.append(
                                Node(NodeType.LEQ, value="<=", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.GE:
                            self.children.append(
                                Node(NodeType.GE, value=">", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.GEQ:
                            self.children.append(
                                Node(NodeType.GEQ, value=">=", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case _:
                            print("Error1")
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                case 5:
                    self.children.append(Node(NodeType.bool_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                    choiceList = [NodeType.AND, NodeType.OR]
                    chosen_element = random.choice(choiceList)
                    match chosen_element:
                        case NodeType.AND:
                            self.children.append(
                                Node(NodeType.AND, value="&&", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.OR:
                            self.children.append(
                                Node(NodeType.OR, value="||", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                    self.children.append(Node(NodeType.bool_value, parent=self,
                                            depth=self.depth - 1, max_width=self.max_width))
                case 6:
                    self.children.append(
                        Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=self.depth - 1,
                            max_width=self.max_width))
                    self.children.append(Node(NodeType.bool_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                    self.children.append(
                        Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=self.depth - 1,
                            max_width=self.max_width))
                case _:
                    raise ValueError("Error during growing bool_value.")

    def grow_numeric_value(self):
        option = random.randint(1, 5)

        if self.children == []: 
            match option:
                case 1:
                    self.children.append(
                        Node(NodeType.NUMBER, value=str(round(random.uniform(MIN_NUMERIC, MAX_NUMERIC),2)), parent=self, isterminal=True,
                            depth=self.depth - 1, max_width=self.max_width))
                case 2:
                    self.children.append(
                        Node(NodeType.NUM_VAR, value="X" + str(random.randint(1, MAX_FUNCTION_DIMENSION)), parent=self,
                            isterminal=True, depth=self.depth - 1, max_width=self.max_width))
                case 3:
                    self.children.append(Node(NodeType.SUB, value="-", parent=self, isterminal=True, depth=self.depth - 1,
                                            max_width=self.max_width))
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                case 4:
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                    choiceList = [NodeType.ADD, NodeType.SUB, NodeType.MUL, NodeType.DIV]
                    chosen_element = random.choice(choiceList)
                    match chosen_element:
                        case NodeType.ADD:
                            self.children.append(
                                Node(NodeType.ADD, value="+", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.SUB:
                            self.children.append(
                                Node(NodeType.SUB, value="-", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.MUL:
                            self.children.append(
                                Node(NodeType.MUL, value="*", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.DIV:
                            self.children.append(
                                Node(NodeType.DIV, value="/", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                case 5:
                    self.children.append(
                        Node(NodeType.LEFTPREN, value="(", parent=self, isterminal=True, depth=self.depth - 1,
                            max_width=self.max_width))
                    self.children.append(Node(NodeType.numeric_value, parent=self, depth=self.depth - 1,
                                            max_width=self.max_width))
                    self.children.append(
                        Node(NodeType.RIGHTPREN, value=")", parent=self, isterminal=True, depth=self.depth - 1,
                            max_width=self.max_width))

                case 9:
                    self.children.append(Node(NodeType.NUM_VAR, value="X" + str(random.randint(1, MAX_FUNCTION_DIMENSION)), parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))

                    choiceList = [ NodeType.SUB, NodeType.MUL, NodeType.DIV, NodeType.ADD]
                    chosen_element = random.choice(choiceList)
                    match chosen_element:
                        case NodeType.ADD:
                            self.children.append(
                                Node(NodeType.ADD, value="+", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.SUB:
                            self.children.append(
                                Node(NodeType.SUB, value="-", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.MUL:
                            self.children.append(
                                Node(NodeType.MUL, value="*", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))
                        case NodeType.DIV:
                            self.children.append(
                                Node(NodeType.DIV, value="/", parent=self, isterminal=True, depth=self.depth - 1,
                                    max_width=self.max_width))

                    self.children.append(Node(NodeType.NUM_VAR, value="X" + str(random.randint(1, MAX_FUNCTION_DIMENSION)), parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))

        
                case _:
                    raise ValueError("Error during growing bool_value.")
                

    def grow(self) -> None:
        match self.node_type:
            case NodeType.program:
                self.grow_program()

            case NodeType.expressions:
                if self.children == []:
                    if self.depth > 0:
                        self.grow_expressions()
                    else:
                        # expression_parent = self.parent
                        # expression_parent.children.remove(self)
                        pass
                else:
                    pass

            case NodeType.if_statement:
                if self.depth > 0:
                    self.grow_if_statement()
                else:
                    # expression = self.parent.parent
                    # expression.children.remove(self.parent)
                    pass

            case NodeType.while_loop:
                if self.depth > 0:
                    self.grow_while_loop()
                else:
                    # expression = self.parent.parent
                    # expression.children.remove(self.parent)
                    pass

            case NodeType.wrtie_val:
                if self.depth > 0:
                    self.grow_write_val()
                else:
                    # expression = self.parent.parent
                    # expression.children.remove(self.parent)
                    pass

            case NodeType.read_var:
                self.grow_read_var()


            case NodeType.assignment:
                if self.depth > 0:
                    self.grow_assignment()
                else:
                    if self.parent.children == []:
                        self.children.append(
                            Node(NodeType.NUM_VAR, value="X" + str(random.randint(1, MAX_FUNCTION_DIMENSION)), parent=self, isterminal=True, depth=self.depth - 1, max_width=self.max_width))
                    else:
                        pass

            case NodeType.bool_value:
                if self.depth > 1:
                    self.grow_bool_value()
                else:
                    if self.children == []:
                        self.children.append(Node(NodeType.FALSE, value="False", parent=self, isterminal=True,
                                                depth=self.depth - 1))
                    else:
                        pass

            case NodeType.numeric_value:
                if self.depth > 1:
                    self.grow_numeric_value()
                else:
                    if self.children == []:
                        self.children.append(
                            Node(NodeType.NUMBER, value=str(round(random.uniform(MIN_NUMERIC, MAX_NUMERIC), 2)), parent=self, isterminal=True,
                                depth=self.depth - 1))
                    else:
                        pass

        self.growChildren()

    def growChildren(self):
        for child in self.children:
            if not child.isterminal:
                child.grow()


def generateTree(depth, width):
    root = Node(NodeType.program, depth=depth, max_width=width)
    root.grow()
    return root


if __name__ == "__main__":
    root = generateTree(14,22)
    root.printTree()

    # arr = [1, 2, 3, 4, 5]
    # del arr[2]
    # print(arr)