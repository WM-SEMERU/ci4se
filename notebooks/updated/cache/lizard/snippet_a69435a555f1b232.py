def stochastic_selection(population, fitnesses):
    pop_size = len(population)
    probabilities = _fitnesses_to_probabilities(fitnesses)
    selection_list = []
    selection_spacing = 1.0 / pop_size
    selection_start = random.uniform(0.0, selection_spacing)
    for i in range(pop_size):
        selection_list.append(selection_start + selection_spacing * i)
    intermediate_population = []
    for selection in selection_list:
        for i, probability in enumerate(probabilities):
            if probability >= selection:
                intermediate_population.append(population[i])
                break
    random.shuffle(intermediate_population)
    return intermediate_population