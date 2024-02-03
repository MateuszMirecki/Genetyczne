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
        parent1_random_node = self.getRandomNodeFasade(parent1)
        parent2_random_node = self.getRandomNodeFasade(parent2)

        counter = 0
        while parent2_random_node.node_type != parent1_random_node.node_type:
            parent2_random_node = self.getRandomNodeFasade(parent2)
            counter += 1
            if counter > 100:
                return RuntimeError("Crossover failed no matching node types found")


        children1 = parent1_random_node.parent.children
        index1 = children1.index(parent1_random_node)

        children2 = parent2_random_node.parent.children
        index2 = children2.index(parent2_random_node)

        children1[index1] = parent2_random_node
        children2[index2] = parent1_random_node


        return parent1


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
    root = generateTree(5, 5)
    root.printTree()
    evolutionOperation.mutation(root)
    root.printTree()