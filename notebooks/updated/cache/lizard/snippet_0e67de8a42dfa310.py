def bound_symbols(self):
    if self._bound_symbols is None:
        res = set.union(set([]), *[_bound_symbols(val) for val in self.
            kwargs.values()])
        res.update(set([]), *[_bound_symbols(arg) for arg in self.args])
        self._bound_symbols = res
    return self._bound_symbols