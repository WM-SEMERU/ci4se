def eccentricity(self, **kw):
    r
    ra = self.apocenter(**kw)
    rp = self.pericenter(**kw)
    return (ra - rp) / (ra + rp)