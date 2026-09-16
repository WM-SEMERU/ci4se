def get_fitness(self, solution):
    return self._fitness_function(solution, *self._fitness_args, **self.
        _fitness_kwargs)