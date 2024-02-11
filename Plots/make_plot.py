import matplotlib.pyplot as plt

def plot_fitness(fitness_function_name):
    # Construct file name from the fitness function name
    filename = f"plot_{fitness_function_name}.txt"
    
    # Initialize lists to hold generations and fitness values
    generations = []
    fitness_values = []
    
    # Read data from file
    with open(filename, 'r') as file:
        for line in file:
            generation, fitness = line.split(',')
            generations.append(int(generation))
            fitness_values.append(float(fitness))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(generations, fitness_values, marker='o', linestyle='-', color='b')
    plt.title(f"Best Fitness Over Generations for {fitness_function_name}")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)
    plt.show()

# Example usage
plot_fitness('1_2_B')
