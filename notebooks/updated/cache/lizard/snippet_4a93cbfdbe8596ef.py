def fill_masked(self, value=-1, copy=True):
    if self.mask is None:
        raise ValueError('no mask is set')
    data = np.array(self.values, copy=copy)
    data[self.mask, ...] = value
    if copy:
        out = type(self)(data)
        out.is_phased = self.is_phased
    else:
        out = self
        out.mask = None
    return out