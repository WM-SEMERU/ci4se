def expand(self, a=None, f=None, lmax=None, lmax_calc=None, sampling=2):
    if a is None:
        a = self.r0
    if f is None:
        f = 0.0
    if lmax is None:
        lmax = self.lmax
    if lmax_calc is None:
        lmax_calc = lmax
    if self.errors is not None:
        coeffs, errors = self.to_array(normalization='schmidt', csphase=1)
    else:
        coeffs = self.to_array(normalization='schmidt', csphase=1)
    rad, theta, phi, total, pot = _MakeMagGridDH(coeffs, self.r0, a=a, f=f,
        lmax=lmax, lmax_calc=lmax_calc, sampling=sampling)
    return _SHMagGrid(rad, theta, phi, total, pot, a, f, lmax, lmax_calc)