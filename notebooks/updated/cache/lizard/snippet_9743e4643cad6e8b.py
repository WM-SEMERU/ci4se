def load_bmus(self, filename):
    self.bmus = np.loadtxt(filename, comments='%', usecols=(1, 2))
    if self.n_vectors != 0 and len(self.bmus) != self.n_vectors:
        raise Exception(
            'The number of best matching units does not match the number of data instances'
            )
    else:
        self.n_vectors = len(self.bmus)
    tmp = self.bmus[:, (0)].copy()
    self.bmus[:, (0)] = self.bmus[:, (1)].copy()
    self.bmus[:, (1)] = tmp
    if max(self.bmus[:, (0)]) > self._n_columns - 1 or max(self.bmus[:, (1)]
        ) > self._n_rows - 1:
        raise Exception(
            'The dimensions of the best matching units do not match that of the map'
            )