def _get_counts(self, f):
    self._consolidate_inplace()
    counts = dict()
    for b in self.blocks:
        v = f(b)
        counts[v] = counts.get(v, 0) + b.shape[0]
    return counts