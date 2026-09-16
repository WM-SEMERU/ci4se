def bbox2path(xmin, xmax, ymin, ymax):
    b = Line(xmin + 1.0j * ymin, xmax + 1.0j * ymin)
    t = Line(xmin + 1.0j * ymax, xmax + 1.0j * ymax)
    r = Line(xmax + 1.0j * ymin, xmax + 1.0j * ymax)
    l = Line(xmin + 1.0j * ymin, xmin + 1.0j * ymax)
    return Path(b, r, t.reversed(), l.reversed())