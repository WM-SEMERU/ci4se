def datapoint(self, ind):
    if self.height is None:
        return self.data[ind]
    return self.data[ind, ...].copy()