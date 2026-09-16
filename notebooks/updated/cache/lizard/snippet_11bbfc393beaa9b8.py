def dimension(self):
    self.dim = 0
    self._slices = {}
    for stochastic in self.stochastics:
        if isinstance(stochastic.value, np.matrix):
            p_len = len(stochastic.value.A.ravel())
        elif isinstance(stochastic.value, np.ndarray):
            p_len = len(stochastic.value.ravel())
        else:
            p_len = 1
        self._slices[stochastic] = slice(self.dim, self.dim + p_len)
        self.dim += p_len