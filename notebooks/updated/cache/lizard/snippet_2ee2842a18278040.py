def drawCurve(self, p1, p2, p3):
    kappa = 0.55228474983
    p1 = Point(p1)
    p2 = Point(p2)
    p3 = Point(p3)
    k1 = p1 + (p2 - p1) * kappa
    k2 = p3 + (p2 - p3) * kappa
    return self.drawBezier(p1, k1, k2, p3)