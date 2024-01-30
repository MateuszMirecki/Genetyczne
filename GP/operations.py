import random
import copy

from Node import Node
from NodeType import NodeType

class EvolutionOperations:


    def mutation(self, root: Node):
        types_for_mutation = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val]

        tree_height = self.tree_height(root)

        random_node_number = random.randint(1,tree_height)

        random_node = self.getRandomNode(root, random_node_number)
        counter = 0
        while(random_node.node_type not in types_for_mutation):
            counter += 1
            if counter > 100:
                print("Mutation failed no matching node types found")
                return None
            if random_node.parent == None:
                random_node_number = random.randint(1, tree_height)
                random_node = self.getRandomNode(root, random_node_number)
            else:
                random_node = random_node.parent

        new_bool_value = Node(node_type=NodeType.bool_value)
        new_bool_value.grow()

        # new_bool_value.printTree()
        # print()

        random_node.children[2] = new_bool_value

        return root

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



    def tree_traversal(self, node: Node):
        if len(node.children) == 0:
            return 1
        for child in self.children:
            return 1 + self.tree_traversal(child)

    def tree_height(self, root):
        number_of_children = len(root.children)

        if number_of_children == 0:
            return 0

        child_1_height = 0
        child_2_height = 0
        child_3_height = 0
        child_4_height = 0
        child_5_height = 0
        child_6_height = 0
        child_7_height = 0

        match number_of_children:
            case 1:
                child_1_height = self.tree_height(root.children[0])
            case 2:
                child_1_height = self.tree_height(root.children[0])
                child_2_height = self.tree_height(root.children[1])
            case 3:
                child_1_height = self.tree_height( root.children[0])
                child_2_height = self.tree_height( root.children[1])
                child_3_height = self.tree_height( root.children[2])
            case 4:
                child_1_height = self.tree_height( root.children[0])
                child_2_height = self.tree_height( root.children[1])
                child_3_height = self.tree_height( root.children[2])
                child_4_height = self.tree_height( root.children[3])
            case 5:
                child_1_height = self.tree_height( root.children[0])
                child_2_height = self.tree_height( root.children[1])
                child_3_height = self.tree_height( root.children[2])
                child_4_height = self.tree_height( root.children[3])
                child_5_height = self.tree_height( root.children[4])
            case 6:
                child_1_height = self.tree_height( root.children[0])
                child_2_height = self.tree_height( root.children[1])
                child_3_height = self.tree_height( root.children[2])
                child_4_height = self.tree_height( root.children[3])
                child_5_height = self.tree_height( root.children[4])
                child_6_height = self.tree_height( root.children[5])
            case 7:
                child_1_height = self.tree_height( root.children[0])
                child_2_height = self.tree_height( root.children[1])
                child_3_height = self.tree_height( root.children[2])
                child_4_height = self.tree_height( root.children[3])
                child_5_height = self.tree_height( root.children[4])
                child_6_height = self.tree_height( root.children[5])
                child_7_height = self.tree_height( root.children[6])


        return max(child_1_height, child_2_height, child_3_height, child_4_height, child_5_height, child_6_height, child_7_height) + 1

    def getRandomNode(self, node, randomNumber):
        # print(f"Getting random node... Current node: {node}, Random number: {randomNumber}")
        if randomNumber == 0 or node.value == None:
            return node
        randomChild = random.choice(node.children)
        # print("getRandomNode: getting randomChild", randomChild)
        return randomChild
        # return self.getRandomNode(randomChild, randomNumber-1)

    def getRandomNodeFasade(self, root):
        # print(f"Entering getRandomNodeFasade... Root: {root}")
        RandomNumber = random.randint(1, self.tree_height(root))
        # print(f"Random number chosen: {RandomNumber}")
        random_node = self.getRandomNode(root, RandomNumber)
        # print(f"Random node chosen: {random_node}")

        if random_node.value == None:
            return random_node
        else:
            return random_node.parent



if __name__ == "__main__":
    evolutionOperations = EvolutionOperations()
    root = Node(NodeType.program)
    root2 = Node(NodeType.program)
    root.grow()
    root2.grow()

    root.printTree()
    print('\n')
    root2.printTree()
    print('\n')

    # evolutionOperations.mutation(root)
    # root.printTree()

    evolutionOperations.crossover(root, root2)
    root.printTree()
    print('\n')

    root2.printTree()
    print('\n')