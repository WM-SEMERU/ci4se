def min(self, values, axis=0):
    values = np.asarray(values)
    return self.unique, self.reduce(values, np.minimum, axis)