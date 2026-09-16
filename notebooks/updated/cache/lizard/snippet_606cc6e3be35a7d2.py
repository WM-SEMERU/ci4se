def get_tables(self):
    if isinstance(self.model, BayesianModel):
        cpds = self.model.get_cpds()
        cpds.sort(key=lambda x: x.variable)
        tables = []
        for cpd in cpds:
            values = list(map(str, cpd.values.ravel()))
            tables.append(values)
        return tables
    elif isinstance(self.model, MarkovModel):
        factors = self.model.get_factors()
        tables = []
        for factor in factors:
            values = list(map(str, factor.values.ravel()))
            tables.append(values)
        return tables
    else:
        raise TypeError(
            'Model must be an instance of Markov or Bayesian model.')