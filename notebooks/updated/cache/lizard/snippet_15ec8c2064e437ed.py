def photbw(self, floor=0):
    mywaveunits = self.waveunits.name
    self.convert('angstroms')
    wave = self.wave
    thru = self.throughput
    self.convert(mywaveunits)
    num = self.trapezoidIntegration(wave, thru * N.log(wave) / wave)
    den = self.trapezoidIntegration(wave, thru / wave)
    if num == 0 or den == 0:
        return 0.0
    avg_wave = N.exp(num / den)
    if floor != 0:
        idx = N.where(thru >= floor)
        wave = wave[idx]
        thru = thru[idx]
    integrand = thru * N.log(wave / avg_wave) ** 2 / wave
    num = self.trapezoidIntegration(wave, integrand)
    if num == 0 or den == 0:
        return 0.0
    return avg_wave * N.sqrt(num / den)