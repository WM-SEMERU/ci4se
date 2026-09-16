def call_hook(self, name, **kwargs):
    return [y for y in [x(**kwargs) for x, _ in self._hooks.get(name, [])] if
        y is not None]