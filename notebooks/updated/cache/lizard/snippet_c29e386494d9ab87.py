def _comparable(self):
    return self._replace(name='' if self.name is None else self.name,
        wavelength=tuple() if self.wavelength is None else self.wavelength,
        resolution=0 if self.resolution is None else self.resolution,
        polarization='' if self.polarization is None else self.polarization,
        calibration='' if self.calibration is None else self.calibration)