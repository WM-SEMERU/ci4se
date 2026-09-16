def transpose(self):

    def _t(item):
        if type(item) == list:
            for n, it in enumerate(item):
                if type(it) == tuple:
                    it = list(it)
                    item[n] = it
                if type(it) == list:
                    _t(it)
                if isinstance(it, np.ndarray) and it.shape == s:
                    item[n] = it.T
    s = self.coeffs['shape']
    for item in self.coeffs.values():
        if type(item) == dict:
            for item2 in item.values():
                _t(item2)
        else:
            _t(item)
    self.coeffs['shape'] = s[::-1]