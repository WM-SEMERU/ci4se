def estimate_hsz(self, R, z=0.0, dR=10.0 ** -8.0, **kwargs):
    Rs = [R - dR / 2.0, R + dR / 2.0]
    sf = numpy.array([self.sigmaz2(r, z, use_physical=False, **kwargs) for
        r in Rs])
    lsf = numpy.log(sf) / 2.0
    return -dR / (lsf[1] - lsf[0])