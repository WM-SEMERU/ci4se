def nonuniform_mutation(random, candidate, args):
    bounder = args['_ec'].bounder
    num_gens = args['_ec'].num_generations
    max_gens = args['max_generations']
    strength = args.setdefault('mutation_strength', 1)
    exponent = (1.0 - num_gens / float(max_gens)) ** strength
    mutant = copy.copy(candidate)
    for i, (c, lo, hi) in enumerate(zip(candidate, bounder.lower_bound,
        bounder.upper_bound)):
        if random.random() <= 0.5:
            new_value = c + (hi - c) * (1.0 - random.random() ** exponent)
        else:
            new_value = c - (c - lo) * (1.0 - random.random() ** exponent)
        mutant[i] = new_value
    return mutant