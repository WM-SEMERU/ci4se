def standardize(self, axis=1):
    if axis == 1:
        return self.map(lambda x: x / std(x))
    elif axis == 0:
        stdval = self.std().toarray()
        return self.map(lambda x: x / stdval)
    else:
        raise Exception('Axis must be 0 or 1')