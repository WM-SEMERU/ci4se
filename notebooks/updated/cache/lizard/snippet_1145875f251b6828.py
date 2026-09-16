def xyz_to_lab(x, y=None, z=None, wref=_DEFAULT_WREF):
    if type(x) in [list, tuple]:
        x, y, z = x
    x /= wref[0]
    y /= wref[1]
    z /= wref[2]
    x, y, z = [(v > 0.008856 and [v ** _oneThird] or [7.787 * v +
        _sixteenHundredsixteenth])[0] for v in (x, y, z)]
    l = 116 * y - 16
    a = 5.0 * (x - y)
    b = 2.0 * (y - z)
    return l, a, b