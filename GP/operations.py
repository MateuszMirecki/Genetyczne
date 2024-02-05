import random
import copy

from Node import Node
from Node import generateTree
from NodeType import NodeType

CROSSOVER_PROBABILITY = 0.95
MUTATION_PROBABILITY = 0.05
ROUNDS_PER_GENERATION = 100
TOURNAMENT_SIZE = 3

class EvolutionOperations:


    def mutation(self, population):
        types_for_mutation = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment]

        program = self.tournament(population, TOURNAMENT_SIZE).program
        program = copy.deepcopy(program)

        # program.printTree()

        random_node = self.getRandomNode(program)

        while(not random_node.node_type in types_for_mutation):
            random_node = self.getRandomNode(program)
        # print(random_node)

        switch_node = Node(random.choice(types_for_mutation), parent=random_node.parent,
                           depth=random_node.depth, max_width=random_node.max_width)
        switch_node.grow()
        # # print(switch_node)
        #
        random_node_children_array_index = random_node.parent.children.index(random_node)
        random_node.parent.children[random_node_children_array_index] = switch_node


        # program.printTree()

        return program


    def crossover(self, population):
        types_for_crossover = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment, NodeType.bool_value, NodeType.numeric_value]

        parent1 = self.tournament(population, TOURNAMENT_SIZE).program
        parent2 = self.tournament(population, TOURNAMENT_SIZE).program

        # parent1.printTree()
        # parent2.printTree()

        parent1 = copy.deepcopy(parent1)
        parent2 = copy.deepcopy(parent2)

        random_node1 = self.getRandomNode(parent1)
        random_node2 = self.getRandomNode(parent2)
        timer = 0

        while random_node1.node_type != random_node2.node_type and random_node1.node_type not in types_for_crossover and random_node2 not in types_for_crossover:
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
                raise ValueError("Crossover failed. No matching nodes found.")


        # print(random_node1.node_type)

        node1_index = random_node1.parent.children.index(random_node1)
        node2_index = random_node2.parent.children.index(random_node2)

        random_node1.parent.children[node1_index] = random_node2
        random_node2.parent.children[node2_index] = random_node1

        random_node1.parent = random_node2.parent
        random_node2.parent = random_node1.parent

        return parent1, parent2



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

    def tournament(self, population, tournament_size: int):
        competitors = random.sample(population, tournament_size)
        return max(competitors, key=lambda x: x.fitness)




class Program:
    def __init__(self, fitness_function, depth: int, max_width: int):
        self.fitness_function = fitness_function
        self.program = generateTree(depth, max_width)
        self.fitness = fitness_function()

    def correctFitness(self):
        self.fitness = self.fitness_function()

class Run:
    def __init__(self, population_size: int, fitness_function, depth: int, max_width: int):
        self.fitness_function = fitness_function
        self.evolutionOperations = EvolutionOperations()
        self.population = self.get_population(fitness_function, depth, max_width, population_size)


    def negative_tournament(self, population, tournament_size: int):
        competitors = random.sample(population, tournament_size)
        worst_competitor = min(competitors, key=lambda x: x.fitness)
        population.remove(worst_competitor)


    def get_population(self, fitness_function, depth: int, max_width: int, population_size: int):
        population = []
        for i in range(population_size):
            population.append(Program(fitness_function, depth, max_width))
        return population

    def get_worst_individual(self, population):
        return min(population, key=lambda x: x.fitness)

    def run(self):
        for _ in range(ROUNDS_PER_GENERATION):
            if random.random() < CROSSOVER_PROBABILITY:
                parent1, parent2 = self.evolutionOperations.crossover(self.population)
                self.negative_tournament(self.population, TOURNAMENT_SIZE)
                self.negative_tournament(self.population, TOURNAMENT_SIZE)
                self.population.append(parent1)
                self.population.append(parent2)
            else:
                self.population.append(self.evolutionOperations.mutation(self.population))
            self.population = self.negative_tournament(self.population, TOURNAMENT_SIZE)







if __name__ == "__main__":
    evolution = EvolutionOperations()
    run = Run(10, 1, 3, 5)
    evolution.mutation(run.population)
