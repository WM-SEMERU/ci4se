def _get_kernel_from_markov_model(self, model):
    self.variables = np.array(model.nodes())
    factors_dict = {var: [] for var in self.variables}
    for factor in model.get_factors():
        for var in factor.scope():
            factors_dict[var].append(factor)
    factors_dict = {var: (factor_product(*factors) if len(factors) > 1 else
        factors[0]) for var, factors in factors_dict.items()}
    self.cardinalities = {var: factors_dict[var].get_cardinality([var])[var
        ] for var in self.variables}
    for var in self.variables:
        other_vars = [v for v in self.variables if var != v]
        other_cards = [self.cardinalities[v] for v in other_vars]
        kernel = {}
        factor = factors_dict[var]
        scope = set(factor.scope())
        for tup in itertools.product(*[range(card) for card in other_cards]):
            states = [State(first_var, s) for first_var, s in zip(
                other_vars, tup) if first_var in scope]
            reduced_factor = factor.reduce(states, inplace=False)
            kernel[tup] = reduced_factor.values / sum(reduced_factor.values)
        self.transition_models[var] = kernel