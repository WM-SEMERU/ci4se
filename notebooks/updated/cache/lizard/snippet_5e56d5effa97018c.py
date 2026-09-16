def copy(self):
    vec = np.copy(self._vec)
    return ScalarCoefs(vec, self.nmax, self.mmax)