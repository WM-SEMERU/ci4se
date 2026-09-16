def strike_dip(self, degrees=True):
    n = self.axes[2]
    r = N.linalg.norm(n)
    strike = N.degrees(N.arctan2(n[0], n[1])) - 90
    dip = N.degrees(N.arccos(n[2] / r))
    if dip > 90:
        dip = 180 - dip
        strike += 180
    if strike < 0:
        strike += 360
    return strike, dip