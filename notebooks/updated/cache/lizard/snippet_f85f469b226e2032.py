def _initial_population_gsa(population_size, solution_size, lower_bounds,
    upper_bounds):
    if len(lower_bounds) != solution_size or len(upper_bounds
        ) != solution_size:
        raise ValueError(
            'Lower and upper bounds much have a length equal to the problem size.'
            )
    return common.make_population(population_size, common.
        random_real_solution, solution_size, lower_bounds, upper_bounds)