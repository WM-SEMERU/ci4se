def getparams(self, result):
    for key in self._cache:
        if self._cache[key][2] == result:
            args, kwargs, _ = self._cache[key]
            return args, kwargs
    else:
        raise ValueError('Result is not cached')