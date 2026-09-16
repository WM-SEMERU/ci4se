def record(self, *args, **kwargs):
    args = [iter(args)] * 2
    positionals = zip(*args)
    for name, value in chain(positionals, kwargs.items()):
        self._recorded_vars[name] = value