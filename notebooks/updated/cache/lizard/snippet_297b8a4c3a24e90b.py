def register(self, pattern, view=None):
    if view is None:
        return partial(self.register, pattern)
    self.patterns.append(self._make_url((pattern, view)))
    return view