def _init_tmatrix(self):
    if self.radius_type == Scatterer.RADIUS_MAXIMUM:
        radius_type = Scatterer.RADIUS_EQUAL_VOLUME
        radius = self.equal_volume_from_maximum()
    else:
        radius_type = self.radius_type
        radius = self.radius
    self.nmax = pytmatrix.calctmat(radius, radius_type, self.wavelength,
        self.m.real, self.m.imag, self.axis_ratio, self.shape, self.ddelt,
        self.ndgs)
    self._tm_signature = (self.radius, self.radius_type, self.wavelength,
        self.m, self.axis_ratio, self.shape, self.ddelt, self.ndgs)