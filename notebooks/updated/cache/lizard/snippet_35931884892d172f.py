def get_parameters(self, prior_type='BDeu', equivalent_sample_size=5,
    pseudo_counts=None):
    parameters = []
    for node in self.model.nodes():
        _equivalent_sample_size = equivalent_sample_size[node] if isinstance(
            equivalent_sample_size, dict) else equivalent_sample_size
        _pseudo_counts = pseudo_counts[node] if pseudo_counts else None
        cpd = self.estimate_cpd(node, prior_type=prior_type,
            equivalent_sample_size=_equivalent_sample_size, pseudo_counts=
            _pseudo_counts)
        parameters.append(cpd)
    return parameters