def options(self, **options):
    self._contexts.append(self._contexts[-1].copy())
    self.set_options(**options)
    try:
        yield
    finally:
        self._contexts.pop(-1)