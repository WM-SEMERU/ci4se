def dot(self, other):
    from pandas.core.frame import DataFrame
    if isinstance(other, (Series, DataFrame)):
        common = self.index.union(other.index)
        if len(common) > len(self.index) or len(common) > len(other.index):
            raise ValueError('matrices are not aligned')
        left = self.reindex(index=common, copy=False)
        right = other.reindex(index=common, copy=False)
        lvals = left.values
        rvals = right.values
    else:
        lvals = self.values
        rvals = np.asarray(other)
        if lvals.shape[0] != rvals.shape[0]:
            raise Exception('Dot product shape mismatch, %s vs %s' % (lvals
                .shape, rvals.shape))
    if isinstance(other, DataFrame):
        return self._constructor(np.dot(lvals, rvals), index=other.columns
            ).__finalize__(self)
    elif isinstance(other, Series):
        return np.dot(lvals, rvals)
    elif isinstance(rvals, np.ndarray):
        return np.dot(lvals, rvals)
    else:
        raise TypeError('unsupported type: %s' % type(other))