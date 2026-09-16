def transform_non_affine(self, s):
    T = self._T
    M = self._M
    W = self._W
    p = self._p
    return T * 10 ** -(M - W) * (10 ** (s - W) - p ** 2 * 10 ** (-(s - W) /
        p) + p ** 2 - 1)