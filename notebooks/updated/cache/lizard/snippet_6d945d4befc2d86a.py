def initialize_pop(self):
    self.toolbox.register('individual', self.generate)
    self.toolbox.register('population', tools.initRepeat, list, self.
        toolbox.individual)
    self.population = self.toolbox.population(n=self._params['popsize'])
    self.assign_fitnesses(self.population)
    self._params['model_count'] += len(self.population)