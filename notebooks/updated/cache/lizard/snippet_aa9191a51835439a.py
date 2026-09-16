def Nu_Griem(Re, Pr, H=None):
    r
    if H:
        if H < 1540000.0:
            w = 0.82
        elif H > 1740000.0:
            w = 1
        else:
            w = 0.82 + 9e-07 * (H - 1540000.0)
    else:
        w = 1
    Nu = 0.0169 * Re ** 0.8356 * Pr ** 0.432 * w
    return Nu