def shift_or_mirror_into_invertible_domain(self, solution_genotype, copy=False
    ):
    assert solution_genotype is not None
    if copy:
        y = [val for val in solution_genotype]
    else:
        y = solution_genotype
    if isinstance(y, np.ndarray) and not isinstance(y[0], float):
        y = array(y, dtype=float)
    for i in rglen(y):
        lb = self._lb[self._index(i)]
        ub = self._ub[self._index(i)]
        al = self._al[self._index(i)]
        au = self._au[self._index(i)]
        if y[i] < lb - 2 * al - (ub - lb) / 2.0 or y[i] > ub + 2 * au + (ub -
            lb) / 2.0:
            r = 2 * (ub - lb + al + au)
            s = lb - 2 * al - (ub - lb) / 2.0
            y[i] -= r * ((y[i] - s) // r)
        if y[i] > ub + au:
            y[i] -= 2 * (y[i] - ub - au)
        if y[i] < lb - al:
            y[i] += 2 * (lb - al - y[i])
    return y