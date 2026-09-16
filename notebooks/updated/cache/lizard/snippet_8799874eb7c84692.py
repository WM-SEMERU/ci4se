def cast_dicts(self, to=DEFAULT, d=DEFAULT):
    if to is DEFAULT:
        to = type(self)
    if d is DEFAULT:
        d = self
    if isinstance(d, list):
        return [v for v in (self.cast_dicts(to, v) for v in d)]
    elif isinstance(d, dict):
        return to({k: v for k, v in ((k, self.cast_dicts(to, v)) for k, v in
            d.items())})
    return d