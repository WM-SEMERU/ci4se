def update(self, other):
    for k, v in other.items():
        if k in self._params:
            assert self._params[k
                ] is v, "Cannot update self with other because they have different Parameters with the same name '%s'" % k
    for k, v in other.items():
        self._params[k] = v