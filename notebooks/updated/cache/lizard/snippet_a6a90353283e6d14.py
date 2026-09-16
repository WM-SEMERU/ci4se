def circumcenter(self):
    if self.isRight:
        return self.hypotenuse.midpoint
    if self.A.isOrigin:
        t = self
    else:
        t = Triangle(self.A - self.A, self.B - self.A, self.C - self.A)
    if not t.A.isOrigin:
        raise ValueError('failed to translate {} to origin'.format(t))
    BmulC = t.B * t.C.yx
    d = 2 * (BmulC.x - BmulC.y)
    bSqSum = sum((t.B ** 2).xy)
    cSqSum = sum((t.C ** 2).xy)
    x = (t.C.y * bSqSum - t.B.y * cSqSum) / d + self.A.x
    y = (t.B.x * cSqSum - t.C.x * bSqSum) / d + self.A.y
    return Point(x, y)