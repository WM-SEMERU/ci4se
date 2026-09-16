def _inverse_i(self, y, i):
    lb = self._lb[self._index(i)]
    ub = self._ub[self._index(i)]
    al = self._al[self._index(i)]
    au = self._au[self._index(i)]
    if 1 < 3:
        if not lb <= y <= ub:
            raise ValueError(
                'argument of inverse must be within the given bounds')
    if y < lb + al:
        return lb - al + 2 * (al * (y - lb)) ** 0.5
    elif y < ub - au:
        return y
    else:
        return ub + au - 2 * (au * (ub - y)) ** 0.5