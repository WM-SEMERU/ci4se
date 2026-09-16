def likelihood_weighted_sample(self, evidence=None, size=1, return_type=
    'dataframe'):
    types = [(var_name, 'int') for var_name in self.topological_order]
    types.append(('_weight', 'float'))
    sampled = np.zeros(size, dtype=types).view(np.recarray)
    sampled['_weight'] = np.ones(size)
    evidence_dict = {var: st for var, st in evidence}
    for node in self.topological_order:
        cpd = self.model.get_cpds(node)
        states = range(self.cardinality[node])
        evidence = cpd.get_evidence()
        if evidence:
            evidence_values = np.vstack([sampled[i] for i in evidence])
            cached_values = self.pre_compute_reduce(node)
            weights = list(map(lambda t: cached_values[tuple(t)],
                evidence_values.T))
            if node in evidence_dict:
                sampled[node] = evidence_dict[node]
                for i in range(size):
                    sampled['_weight'][i] *= weights[i][evidence_dict[node]]
            else:
                sampled[node] = sample_discrete(states, weights)
        elif node in evidence_dict:
            sampled[node] = evidence_dict[node]
            for i in range(size):
                sampled['_weight'][i] *= cpd.values[evidence_dict[node]]
        else:
            sampled[node] = sample_discrete(states, cpd.values, size)
    return _return_samples(return_type, sampled)