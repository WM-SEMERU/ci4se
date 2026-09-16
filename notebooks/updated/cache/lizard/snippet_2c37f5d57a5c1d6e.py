def where(cond, a, b, use_numexpr=True):
    if use_numexpr:
        return _where(cond, a, b)
    return _where_standard(cond, a, b)