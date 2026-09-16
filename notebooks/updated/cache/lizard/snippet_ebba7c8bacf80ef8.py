def unit_tangent(self, t=None):
    assert self.end != self.start
    dseg = self.end - self.start
    return dseg / abs(dseg)