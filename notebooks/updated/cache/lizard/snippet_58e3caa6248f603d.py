def argrange(self, axis=None):
    amin = self.argmin(axis=axis)
    amax = self.argmax(axis=axis)
    if axis is None:
        return amin, amax
    else:
        return np.stack([amin, amax]).T