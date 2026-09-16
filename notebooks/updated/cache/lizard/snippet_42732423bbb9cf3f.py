def _seed(self, seed=-1):
    if seed != -1:
        self._random = np.random.RandomState(seed)
    else:
        self._random = np.random.RandomState()