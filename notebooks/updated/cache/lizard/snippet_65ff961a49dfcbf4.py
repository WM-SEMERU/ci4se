def rgb_to_hsl(r, g=None, b=None):
    if type(r) in [list, tuple]:
        r, g, b = r
    minVal = min(r, g, b)
    maxVal = max(r, g, b)
    l = (maxVal + minVal) / 2.0
    if minVal == maxVal:
        return 0.0, 0.0, l
    d = maxVal - minVal
    if l < 0.5:
        s = d / (maxVal + minVal)
    else:
        s = d / (2.0 - maxVal - minVal)
    dr, dg, db = [((maxVal - val) / d) for val in (r, g, b)]
    if r == maxVal:
        h = db - dg
    elif g == maxVal:
        h = 2.0 + dr - db
    else:
        h = 4.0 + dg - dr
    h = h * 60.0 % 360.0
    return h, s, l