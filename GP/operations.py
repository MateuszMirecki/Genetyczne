import random
import copy

from Node import Node
from Node import generateTree
from NodeType import NodeType

import GP.fitnes_functions

CROSSOVER_PROBABILITY = 0.95
MUTATION_PROBABILITY = 0.05
ROUNDS_PER_GENERATION = 100
GENERATION_NUMBER = 100
TOURNAMENT_SIZE = 3


class EvolutionOperations:


    def mutation(self, population):
        types_for_mutation = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                              NodeType.read_var, NodeType.assignment]

        new_program_class = self.tournament(population, TOURNAMENT_SIZE)
        new_program_class_copy = copy.deepcopy(new_program_class)
        program = new_program_class_copy.program

            # test mutation
        # program.printTree()
        # print()

        random_node = self.getRandomNode(program)

        while(not random_node.node_type in types_for_mutation):
            random_node = self.getRandomNode(program)



        switch_node = Node(random.choice(types_for_mutation), parent=random_node.parent,
                           depth=random_node.depth, max_width=random_node.max_width)
        switch_node.grow()




        random_node_children_array_index = random_node.parent.children.index(random_node)
        random_node.parent.children[random_node_children_array_index] = switch_node

            # mutation test
        # program.printTree()

        new_program_class.correctFitness()
        return new_program_class_copy


    def crossover(self, population):
        types_for_crossover = [NodeType.if_statement, NodeType.while_loop, NodeType.wrtie_val,
                               NodeType.read_var, NodeType.assignment, NodeType.bool_value, NodeType.numeric_value]

        new_program_class_1 = self.tournament(population, TOURNAMENT_SIZE)
        new_program_class_2 = self.tournament(population, TOURNAMENT_SIZE)

        while new_program_class_1 is new_program_class_2:
            new_program_class_2 = self.tournament(population, TOURNAMENT_SIZE)

        new_program_class_1 = copy.deepcopy(new_program_class_1)
        new_program_class_2 = copy.deepcopy(new_program_class_2)


        parent1 = new_program_class_1.program
        parent2 = new_program_class_2.program

            # crossover test
        # parent1.printTree()
        # parent2.printTree()
        # print()

        random_node1 = self.getRandomNode(parent1)
        random_node2 = self.getRandomNode(parent2)

        timer1 = 0
        timer2 = 0
        isCompatible = False


        firstBool = random_node1.node_type not in types_for_crossover
        secondBool = random_node2.node_type not in types_for_crossover
        thirdBool = random_node1.node_type != random_node2.node_type


        while (firstBool or secondBool) or thirdBool:
            random_node1 = self.getRandomNode(parent1)

            while (firstBool or secondBool) or thirdBool:
                random_node2 = self.getRandomNode(parent2)
                timer1 += 1

                if random_node1.node_type == random_node2.node_type and random_node1.node_type in types_for_crossover and random_node2.node_type in types_for_crossover:
                    isCompatible = True
                    break

                if timer1 > 1000:
                    timer1 = 0
                    break

            if isCompatible:

                break

            timer2 += 1
            if timer2 > 1000:
                print("error")
                raise RuntimeError("No compatible nodes for crossover")


        random_node1_copy = copy.deepcopy(random_node1)
        random_node2_copy = copy.deepcopy(random_node2)

        # I
        random_node1_copy.parent = random_node2.parent
        random_node2_copy.parent = random_node1.parent

        # II

        index_node_1 = random_node1.parent.children.index(random_node1)
        index_node_2 = random_node2.parent.children.index(random_node2)

        random_node1.parent.children[index_node_1] = random_node2_copy
        random_node2.parent.children[index_node_2] = random_node1_copy


        # print(random_node1.node_type,'---------', random_node2.node_type,'\n')
        # parent1.printTree()
        # parent2.printTree()
        # print('-----------------------------------------')


        new_program_class_1.correctFitness()
        new_program_class_2.correctFitness()

        return new_program_class_1, new_program_class_2



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
        competitors = random.sample(population, 2)

        # print(len(competitors))
        # for competitor in competitors:
        #     competitor.program.printTree()
        # print('------------------')

        return max(competitors, key=lambda x: x.fitness)




class Program:
    def __init__(self, fitness_function, depth: int, max_width: int, fittness_function_name: str) -> None:
        self.fitness_function = fitness_function
        self.program = generateTree(depth, max_width)
        self.fitness = fitness_function(self.program, fittness_function_name)
        self.fittness_function_name = fittness_function_name

    def correctFitness(self):
        self.fitness = self.fitness_function(self.program, self.fittness_function_name)

class Run:
    def __init__(self, population_size: int, fitness_function, depth: int, max_width: int, fittness_function_name: str):
        self.fitness_function = fitness_function
        self.evolutionOperations = EvolutionOperations()
        self.population = self.get_population(fitness_function, depth, max_width, population_size, fittness_function_name)
        self.fitness_function_name = fittness_function_name


    def negative_tournament(self, tournament_size: int):
        competitors = random.sample(self.population, tournament_size)
        worst_competitor = min(competitors, key=lambda x: x.fitness)
        self.population.remove(worst_competitor)



    def get_population(self, fitness_function, depth: int, max_width: int, population_size: int, fitness_function_name)->list[Program]:
        population = []
        for i in range(population_size):
            population.append(Program(fitness_function, depth, max_width, fitness_function_name))
        return population

    def get_worst_individual(self, population):
        return min(population, key=lambda x: x.fitness)


    def check_if_population_is_correct(self, population):
        for program_class in population:
            if program_class.fitness == 0:
                return program_class
                print("Correct program found")
                program_class.program.printTree()
        return False

    def print_generation_info(self, generation_number):
        best_individual = max(self.population, key=lambda x: x.fitness)
        best_fitness = best_individual.fitness
        print(f"Generation: {generation_number}")
        print(f"Best fitness: {best_fitness} for:")
        best_individual.program.printTree()
        print('---------------------------------')


    def run(self):
        generationNumber = 0
        for _ in range(GENERATION_NUMBER):
            for _ in range(ROUNDS_PER_GENERATION):
                if random.random() < CROSSOVER_PROBABILITY:
                    program1, program2 = self.evolutionOperations.crossover(self.population)
                    self.negative_tournament(TOURNAMENT_SIZE)
                    self.negative_tournament(TOURNAMENT_SIZE)
                    self.population.append(program1)
                    self.population.append(program2)

                if random.random() < MUTATION_PROBABILITY:
                    program_class = self.evolutionOperations.mutation(self.population)
                    self.negative_tournament(TOURNAMENT_SIZE)
                    self.population.append(program_class)

            self.print_generation_info(generationNumber)

            if self.check_if_population_is_correct(self.population):
                print(f"Correct program found during generation {generationNumber}.")
                program_class = self.check_if_population_is_correct(self.population)
                program_class.program.printTree()
                return

            generationNumber += 1


if __name__ == "__main__":
    evolution = EvolutionOperations()

        # crossover test
    # run = Run(3, GP.fitnes_functions.calculate_fitness_function, 6, 6, "1_1_A")
    #
    # fitnes_list = list(map(lambda x: x.fitness, run.population))
    # print(fitnes_list)
    # for program in run.population:
    #     program.program.printTree()
    #
    # program_class1, program_class_2 = evolution.crossover(run.population)
    #
    # run.negative_tournament(TOURNAMENT_SIZE)
    # run.negative_tournament(TOURNAMENT_SIZE)
    #
    # run.population.append(program_class1)
    # run.population.append(program_class_2)
    #
    # print('------------------')
    #
    # fitnes_list = list(map(lambda x: x.fitness, run.population))
    # print(fitnes_list)
    # for program in run.population:
    #     program.program.printTree()



        # mutation test
    # run = Run(10, GP.fitnes_functions.calculate_fitness_function, 3, 6,"1_1_A")
    # program_class1 = evolution.mutation(run.population)


        # Run test
    run = Run(100, GP.fitnes_functions.calculate_fitness_function, 6, 6,"1_1_A")
    run.run()

    print()
    fitness_list = list(map(lambda x: x.fitness, run.population))
    print(fitness_list)




