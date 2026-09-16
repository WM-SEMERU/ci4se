def bpoints2bezier(bpoints):
    order = len(bpoints) - 1
    if order == 3:
        return CubicBezier(*bpoints)
    elif order == 2:
        return QuadraticBezier(*bpoints)
    elif order == 1:
        return Line(*bpoints)
    else:
        assert len(bpoints) in {2, 3, 4}