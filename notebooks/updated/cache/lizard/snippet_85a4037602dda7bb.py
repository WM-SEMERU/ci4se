def _poly_eval_0(self, u, ids):
    return u * (u * (self._a[ids] * u + self._b[ids]) + self._c[ids]
        ) + self._d[ids]