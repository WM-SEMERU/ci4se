def decimaltimestamp(t=None):
    t = time.time() if t is None else t
    return Decimal('{:.6f}'.format(t))