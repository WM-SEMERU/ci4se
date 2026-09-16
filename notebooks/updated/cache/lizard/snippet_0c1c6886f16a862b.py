def compute():
    if what == 'numpy':
        y = eval(expr)
    else:
        y = ne.evaluate(expr)
    return len(y)