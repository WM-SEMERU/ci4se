def rgba_floats_tuple(self, x):
    if x <= self.index[0]:
        return self.colors[0]
    if x >= self.index[-1]:
        return self.colors[-1]
    i = len([u for u in self.index if u < x])
    if self.index[i - 1] < self.index[i]:
        p = (x - self.index[i - 1]) * 1.0 / (self.index[i] - self.index[i - 1])
    elif self.index[i - 1] == self.index[i]:
        p = 1.0
    else:
        raise ValueError('Thresholds are not sorted.')
    return tuple((1.0 - p) * self.colors[i - 1][j] + p * self.colors[i][j] for
        j in range(4))