def _zmaxFindStart(z, Ez, pot):
    if z == 0.0:
        ztry = 1e-05
    else:
        ztry = 2.0 * nu.fabs(z)
    while Ez - potentialVertical(ztry, pot) > 0.0:
        ztry *= 2.0
        if ztry > 100.0:
            raise OverflowError
    return ztry