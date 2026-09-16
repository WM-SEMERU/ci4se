def sd(self):
    v = self.var()
    if len(v):
        return np.sqrt(v)
    else:
        return None