def norm(self, x):
    return float(np.sqrt(self.inner(x, x).real))