def rgb_to_hsv(r, g=None, b=None):
    if type(r) in [list, tuple]:
        r, g, b = r
    v = float(max(r, g, b))
    d = v - min(r, g, b)
    if d == 0:
        return 0.0, 0.0, v
    s = d / v
    dr, dg, db = [((v - val) / d) for val in (r, g, b)]
    if r == v:
        h = db - dg
    elif g == v:
        h = 2.0 + dr - db
    else:
        h = 4.0 + dg - dr
    h = h * 60.0 % 360.0
    return h, s, v