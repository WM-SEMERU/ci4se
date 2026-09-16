def OR(*fns):
    if len(fns) < 2:
        raise TypeError('At least two functions must be passed')

    @chainable
    def validator(v):
        for fn in fns:
            last = None
            try:
                return fn(v)
            except ValueError as err:
                last = err
        if last:
            raise last
    return validator