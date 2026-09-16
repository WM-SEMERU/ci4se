def generation_termination(population, num_generations, num_evaluations, args):
    max_generations = args.setdefault('max_generations', 1)
    return num_generations >= max_generations