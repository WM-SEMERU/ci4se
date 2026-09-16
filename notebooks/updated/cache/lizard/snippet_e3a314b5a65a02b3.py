def _expand(self, coeffsin, nmax):
    if self.coeffs is None:
        self.rotate(clat=90.0, clon=0.0, nrot=nmax)
        falpha = _shtools.SlepianCoeffs(self.coeffs, coeffsin, self.nrot)
    else:
        falpha = _shtools.SlepianCoeffs(self.coeffs, coeffsin, self.nrot)
    return SlepianCoeffs(falpha, self)