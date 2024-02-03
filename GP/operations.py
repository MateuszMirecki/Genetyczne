import random
import copy

from Node import Node
from Node import generateTree
from NodeType import NodeType

class EvolutionOperations:


    def mutation(self, root: Node):
        types_for_mutation = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment]

        random_node = self.getRandomNode(root)
        while(not random_node.node_type in types_for_mutation):
            random_node = self.getRandomNode(root)
        # print(random_node)

        switch_node = Node(random.choice(types_for_mutation), parent=random_node.parent,
                           depth=random_node.depth, max_width=random_node.max_width)
        switch_node.grow()
        # print(switch_node)

        random_node_children_array_index = random_node.parent.children.index(random_node)
        random_node.parent.children[random_node_children_array_index] = switch_node

    ####
    #TRUNIEJ#
    #####

    def tournament(self):
        pass

    ####
    #FITTNESS#
    #####

    

    def crossover(self, parent1: Node, parent2: Node):
        types_for_crossover = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment, NodeType.bool_value, NodeType.numeric_value]

        random_node1 = self.getRandomNode(parent1)
        random_node2 = self.getRandomNode(parent2)
        timer = 0

        while random_node1.node_type != random_node2.node_type:
            random_node1 = self.getRandomNode(parent1)
            while (not random_node1.node_type in types_for_crossover):
                random_node1 = self.getRandomNode(parent1)
            random_node2 = self.getRandomNode(parent2)
            rounds = 0
            while (random_node1.node_type != random_node2.node_type):
                random_node2 = self.getRandomNode(parent2)
                rounds += 1
                if rounds > 1000:
                    rounds = 0
                    break
            timer += 1
            if timer > 100:
                raise ValueError(f"Crossover failed. No {random_node1.node_type} found in parent1.")

        # print(random_node1.node_type)
        node1_index = random_node1.parent.children.index(random_node1)
        node2_index = random_node2.parent.children.index(random_node2)

        random_node1.parent.children[node1_index] = random_node2
        random_node2.parent.children[node2_index] = random_node1

        random_node1.parent = random_node2.parent
        random_node2.parent = random_node1.parent






    # def tree_traversal(self, node: Node):
    #     if len(node.children) == 0:
    #         return 1
    #     for child in self.children:
    #         return 1 + self.tree_traversal(child)

    def tree_height(self, root):
        if len(root.children) == 0:
            return 0

        # Initialize maximum height to 0
        max_height = 0

        # Iterate over all children
        for child in root.children:
            # Calculate the height of the current child
            child_height = self.tree_height(child)
            # Update maximum height if current child's height is greater
            max_height = max(max_height, child_height)

        # Return maximum height of all children plus 1
        return max_height + 1

    def getRandomNode(self, root: Node)->Node:
        random_node_number = random.randint(1, self.tree_height(root)-1)
        # print(5 - random_node_number)
        while random_node_number > 0 and len(root.children) > 0:
            random_node_number -= 1
            root = random.choice(root.children)
        return root


if __name__ == "__main__":
    evolutionOperation = EvolutionOperations()

    root = generateTree(3, 5)
    root2 = generateTree(3, 5)

        # mutation
    # root.printTree()
    # evolutionOperation.mutation(root)
    # root.printTree()

        # crossover
    root.printTree()
    root2.printTree()
    evolutionOperation.crossover(root, root2)
    print()
    root.printTree()
    root2.printTree()
