def _lval_add_towards_polarity(x, polarity):
    if x < 0:
        if polarity < 0:
            return Lval('toinf', x)
        return Lval('pastzero', x)
    elif polarity > 0:
        return Lval('toinf', x)
    return Lval('pastzero', x)