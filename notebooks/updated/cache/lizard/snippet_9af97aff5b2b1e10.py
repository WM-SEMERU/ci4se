def rgb2hsl(rgb):
    r, g, b = [float(v) for v in rgb]
    for name, v in {'Red': r, 'Green': g, 'Blue': b}.items():
        if not 0 - FLOAT_ERROR <= v <= 1 + FLOAT_ERROR:
            raise ValueError('%s must be between 0 and 1. You provided %r.' %
                (name, v))
    vmin = min(r, g, b)
    vmax = max(r, g, b)
    diff = vmax - vmin
    vsum = vmin + vmax
    l = vsum / 2
    if diff < FLOAT_ERROR:
        return 0.0, 0.0, l
    if l < 0.5:
        s = diff / vsum
    else:
        s = diff / (2.0 - vsum)
    dr = ((vmax - r) / 6 + diff / 2) / diff
    dg = ((vmax - g) / 6 + diff / 2) / diff
    db = ((vmax - b) / 6 + diff / 2) / diff
    if r == vmax:
        h = db - dg
    elif g == vmax:
        h = 1.0 / 3 + dr - db
    elif b == vmax:
        h = 2.0 / 3 + dg - dr
    if h < 0:
        h += 1
    if h > 1:
        h -= 1
    return h, s, l