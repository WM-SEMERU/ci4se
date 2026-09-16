def add_population(self, pop):
    if pop.model in self.modelnames:
        raise ValueError('%s model already in PopulationSet.' % pop.model)
    self.modelnames.append(pop.model)
    self.shortmodelnames.append(pop.modelshort)
    self.poplist.append(pop)