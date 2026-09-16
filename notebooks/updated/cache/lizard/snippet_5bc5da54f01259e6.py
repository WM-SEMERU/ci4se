def is_satisfied(self, x_cat):
    satisfied = []
    if self.is_default():
        return np.ones(x_cat.shape[0], dtype=bool)
    for idx, cat in self.clauses:
        satisfied.append(x_cat[:, (idx)] == cat)
    return reduce(np.logical_and, satisfied)