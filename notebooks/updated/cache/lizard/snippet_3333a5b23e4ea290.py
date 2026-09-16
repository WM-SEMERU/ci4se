def is_in_interval(n, l, r, border='included'):
    if 'included' == border:
        return n >= l and n <= r
    elif 'excluded' == border:
        return n > l and n < r
    else:
        raise ValueError("borders must be either 'included' or 'excluded'")