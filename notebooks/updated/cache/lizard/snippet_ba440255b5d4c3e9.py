def define_operators(cls, operators):
    old_ops = dict(cls._operators)
    for op, func in operators.items():
        cls._operators[op] = func
    yield
    cls._operators = old_ops