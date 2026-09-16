def check_model(self):
    for node in super(DynamicBayesianNetwork, self).nodes():
        cpd = self.get_cpds(node=node)
        if isinstance(cpd, TabularCPD):
            evidence = cpd.variables[:0:-1]
            evidence_card = cpd.cardinality[:0:-1]
            parents = self.get_parents(node)
            if set(evidence) != set(parents if parents else []):
                raise ValueError(
                    "CPD associated with {node} doesn't have proper parents associated with it."
                    .format(node=node))
            if not np.allclose(cpd.to_factor().marginalize([node], inplace=
                False).values.flatten('C'), np.ones(np.product(
                evidence_card)), atol=0.01):
                raise ValueError(
                    'Sum of probabilities of states for node {node} is not equal to 1'
                    .format(node=node))
    return True