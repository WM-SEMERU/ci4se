def mjd2gmst(mjd):
    tu = (mjd - MJD0) / (100 * DPY)
    st = math.fmod(mjd, 1.0) * D2PI + (24110.54841 + (8640184.812866 + (
        0.093104 - 6.2e-06 * tu) * tu) * tu) * DS2R
    w = math.fmod(st, D2PI)
    if w >= 0.0:
        return w
    else:
        return w + D2PI