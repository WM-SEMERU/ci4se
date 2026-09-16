def scale(cls, *scaling):
    if len(scaling) == 1:
        sx = sy = float(scaling[0])
    else:
        sx, sy = scaling
    return tuple.__new__(cls, (sx, 0.0, 0.0, 0.0, sy, 0.0, 0.0, 0.0, 1.0))