def _calc(self, y, w):
    if self.discrete:
        self.lclass_ids = weights.lag_categorical(w, self.class_ids, ties=
            'tryself')
    else:
        ly = weights.lag_spatial(w, y)
        self.lclass_ids, self.lag_cutoffs, self.m = self._maybe_classify(ly,
            self.m, self.lag_cutoffs)
        self.lclasses = np.arange(self.m)
    T = np.zeros((self.m, self.k, self.k))
    n, t = y.shape
    for t1 in range(t - 1):
        t2 = t1 + 1
        for i in range(n):
            T[self.lclass_ids[i, t1], self.class_ids[i, t1], self.class_ids
                [i, t2]] += 1
    P = np.zeros_like(T)
    for i, mat in enumerate(T):
        row_sum = mat.sum(axis=1)
        row_sum = row_sum + (row_sum == 0)
        p_i = np.matrix(np.diag(1.0 / row_sum) * np.matrix(mat))
        P[i] = p_i
    return T, P