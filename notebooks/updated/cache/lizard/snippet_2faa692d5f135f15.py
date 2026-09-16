def _Rzderiv(self, R, z, phi=0.0, t=0.0):
    raise AttributeError
    r = numpy.sqrt(R ** 2.0 + z ** 2.0)
    out = self._scf.Rzderiv(R, z, phi=phi, use_physical=False)
    for a, ds, d2s, H, dH in zip(self._Sigma_amp, self._dsigmadR, self.
        _d2SigmadR2, self._Hz, self._dHzdz):
        out += 4.0 * numpy.pi * a * (H(z) * R * z / r ** 2.0 * (d2s(r) - ds
            (r) / r) + ds(r) * dH(z) * R / r)
    return out