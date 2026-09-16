def paramsarraybounds(self):
    bounds = []
    for i, param in self._index_to_param.items():
        if isinstance(param, str):
            bounds.append(self.model.PARAMLIMITS[param])
        elif isinstance(param, tuple):
            bounds.append(self.model.PARAMLIMITS[param[0]])
        else:
            raise ValueError('Invalid param type')
    bounds = [(tup[0] + ALMOST_ZERO, tup[1] - ALMOST_ZERO) for tup in bounds]
    assert len(bounds) == len(self._index_to_param)
    return tuple(bounds)