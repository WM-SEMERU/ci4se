def as_spectrum(self, binned=True):
    if binned:
        wave, flux = self.binwave, self.binflux
    else:
        wave, flux = self.wave, self.flux
    result = ArraySourceSpectrum(wave, flux, self.waveunits, self.fluxunits,
        name=self.name, keepneg=True)
    return result