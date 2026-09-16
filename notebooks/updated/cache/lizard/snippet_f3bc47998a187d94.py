def rand(self, n=1):
    if n == 1:
        return self._rand1()
    else:
        out = np.empty((n, self._p, self._p))
        for i in range(n):
            out[i] = self._rand1()
        return out