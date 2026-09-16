def barlam(self, wavelengths=None):
    x = self._validate_wavelengths(wavelengths).value
    y = self(x).value
    num = np.trapz(y * np.log(x) / x, x=x)
    den = np.trapz(y / x, x=x)
    if num == 0 or den == 0:
        bar_lam = 0.0
    else:
        bar_lam = np.exp(abs(num / den))
    return bar_lam * self._internal_wave_unit