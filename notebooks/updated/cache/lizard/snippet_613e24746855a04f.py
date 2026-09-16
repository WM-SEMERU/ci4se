def equilateral(cls, origin=None, side=1):
    o = Point(origin)
    base = o.x + side
    h = 0.5 * Sqrt_3 * side + o.y
    return cls(o, [base, o.y], [base / 2, h])