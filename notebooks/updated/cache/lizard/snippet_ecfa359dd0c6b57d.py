def endBy(p, sep):
    return separated(p, sep, 0, maxt=float('inf'), end=True)