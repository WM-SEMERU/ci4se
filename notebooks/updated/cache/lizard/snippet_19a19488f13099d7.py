def pivot(self, wavelengths=None):
    x = self._validate_wavelengths(wavelengths).value
    y = self(x).value
    num = np.trapz(y * x, x=x)
    den = np.trapz(y / x, x=x)
    if den == 0:
        pivwv = 0.0
    else:
        pivwv = np.sqrt(abs(num / den))
    return pivwv * self._internal_wave_unit