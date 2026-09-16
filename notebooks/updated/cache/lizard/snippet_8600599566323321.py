def find_abbreviations(self, kwargs):
    new_kwargs = []
    try:
        sig = self.signature()
    except (ValueError, TypeError):
        return [(key, value, value) for key, value in kwargs.items()]
    for param in sig.parameters.values():
        for name, value, default in _yield_abbreviations_for_parameter(param,
            kwargs):
            if value is empty:
                raise ValueError(
                    'cannot find widget or abbreviation for argument: {!r}'
                    .format(name))
            new_kwargs.append((name, value, default))
    return new_kwargs