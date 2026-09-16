def initialize(self, initialization_order=None):
    if self.time is None:
        if self.time_initialization is None:
            self.time = Time()
        else:
            self.time = self.time_initialization()
    self.components._init_outer_references({'scope': self, 'time': self.time})
    remaining = set(self._stateful_elements)
    while remaining:
        progress = set()
        for element in remaining:
            try:
                element.initialize()
                progress.add(element)
            except (KeyError, TypeError, AttributeError):
                pass
        if progress:
            remaining.difference_update(progress)
        else:
            raise KeyError(
                'Unresolvable Reference: Probable circular initialization' +
                '\n'.join([repr(e) for e in remaining]))