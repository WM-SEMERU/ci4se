def rollforward(self, dt):
    dt = as_timestamp(dt)
    if not self.onOffset(dt):
        dt = dt + self.__class__(1, normalize=self.normalize, **self.kwds)
    return dt