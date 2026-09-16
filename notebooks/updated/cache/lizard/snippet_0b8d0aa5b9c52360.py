def _shift_or_mirror_into_invertible_i(self, x, i):
    assert x is not None
    lb = self._lb[self._index(i)]
    ub = self._ub[self._index(i)]
    al = self._al[self._index(i)]
    au = self._au[self._index(i)]
    if x < lb - 2 * al - (ub - lb) / 2.0 or x > ub + 2 * au + (ub - lb) / 2.0:
        r = 2 * (ub - lb + al + au)
        s = lb - 2 * al - (ub - lb) / 2.0
        x -= r * ((x - s) // r)
    if x > ub + au:
        x -= 2 * (x - ub - au)
    if x < lb - al:
        x += 2 * (lb - al - x)
    return x