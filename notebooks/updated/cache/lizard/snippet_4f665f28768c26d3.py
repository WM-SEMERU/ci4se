def rejection_sample(self, evidence=None, size=1, return_type='dataframe'):
    if evidence is None:
        return self.forward_sample(size)
    types = [(var_name, 'int') for var_name in self.topological_order]
    sampled = np.zeros(0, dtype=types).view(np.recarray)
    prob = 1
    i = 0
    while i < size:
        _size = int((size - i) / prob * 1.5)
        _sampled = self.forward_sample(_size, 'recarray')
        for evid in evidence:
            _sampled = _sampled[_sampled[evid[0]] == evid[1]]
        prob = max(len(_sampled) / _size, 0.01)
        sampled = np.append(sampled, _sampled)[:size]
        i += len(_sampled)
    return _return_samples(return_type, sampled)