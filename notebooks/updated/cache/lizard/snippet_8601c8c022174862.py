def select(*cases):
    if len(cases) == 0:
        return
    if isinstance(cases[0], list):
        if len(cases) != 1:
            raise TypeError(
                'Select can be called either with a list of cases or multiple case arguments, but not both.'
                )
        cases = cases[0]
        if not cases:
            return
    default = None
    for c in cases:
        if c.ready():
            return c, c.exec_()
        if isinstance(c, dcase):
            assert default is None, 'Only one default case is allowd.'
            default = c
    if default is not None:
        return default, None
    if _be.would_deadlock():
        raise _Deadlock('No other tasklets running, cannot select.')
    while True:
        for c in cases:
            if c.ready():
                return c, c.exec_()
        _be.yield_()