def _sample(probabilities, population_size):
    population = []
    for _ in range(population_size):
        solution = []
        for probability in probabilities:
            if random.uniform(0.0, 1.0) < probability:
                solution.append(1)
            else:
                solution.append(0)
        population.append(solution)
    return population