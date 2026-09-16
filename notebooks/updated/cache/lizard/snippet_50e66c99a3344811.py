def asof_locs(self, where, mask):
    locs = self.values[mask].searchsorted(where.values, side='right')
    locs = np.where(locs > 0, locs - 1, 0)
    result = np.arange(len(self))[mask].take(locs)
    first = mask.argmax()
    result[(locs == 0) & (where.values < self.values[first])] = -1
    return result