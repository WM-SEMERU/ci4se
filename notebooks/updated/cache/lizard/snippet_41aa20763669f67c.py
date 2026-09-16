def rotate(p, rad, o=(0, 0)):
    v = vector(o, p)
    fx = lambda x, y, d: x * cos(d) - y * sin(d)
    fy = lambda x, y, d: x * sin(d) + y * cos(d)
    rv = fx(v[0], v[1], rad), fy(v[0], v[1], rad)
    return translate(rv, o)