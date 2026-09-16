def is_imap(self, JPD):
    if not isinstance(JPD, JointProbabilityDistribution):
        raise TypeError(
            'JPD must be an instance of JointProbabilityDistribution')
    factors = [cpd.to_factor() for cpd in self.get_cpds()]
    factor_prod = reduce(mul, factors)
    JPD_fact = DiscreteFactor(JPD.variables, JPD.cardinality, JPD.values)
    if JPD_fact == factor_prod:
        return True
    else:
        return False