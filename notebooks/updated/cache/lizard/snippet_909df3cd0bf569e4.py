def clip(self, min=None, max=None):
    return self._constructor(self.values.clip(min=min, max=max)).__finalize__(
        self)