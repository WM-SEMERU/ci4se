def Or(*xs, simplify=True):
    xs = [Expression.box(x).node for x in xs]
    y = exprnode.or_(*xs)
    if simplify:
        y = y.simplify()
    return _expr(y)