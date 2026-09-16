def disvec(self, x, y, aq=None):
    if aq is None:
        aq = self.model.aq.find_aquifer_data(x, y)
    return np.sum(self.parameters * self.disvecinf(x, y, aq), 1)