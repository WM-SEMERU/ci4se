def grid(fitness_function, no_dimensions, step_size):
    best_fitness = float('-inf')
    best_arguments = None
    for arguments in make_lists(no_dimensions, step_size):
        fitness = fitness_function(tuple(arguments))
        if fitness > best_fitness:
            best_fitness = fitness
            best_arguments = tuple(arguments)
    return best_arguments