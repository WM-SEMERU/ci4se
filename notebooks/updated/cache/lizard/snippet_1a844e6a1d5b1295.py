def initial_individual(self):
    ind = creator.Individual([random.uniform(-1, 1) for _ in range(len(self
        ._params['value_means']))])
    return ind