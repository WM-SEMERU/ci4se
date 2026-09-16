def model_mag(self, pardict, use_cache=True):
    if pardict == self._cache_key and use_cache:
        return self._cache_val
    self._cache_key = pardict
    p = []
    for l in self.leaf_labels:
        p.extend(pardict[l])
    assert len(p) == self.n_params
    tot = np.inf
    for i, m in enumerate(self.leaves):
        mag = m.evaluate(p[i * 5:(i + 1) * 5], self.band)
        tot = addmags(tot, mag)
    self._cache_val = tot
    return tot