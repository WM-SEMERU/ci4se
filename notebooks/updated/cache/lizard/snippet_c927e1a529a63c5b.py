def trimSpectrum(sp, minw, maxw):
    wave = sp.GetWaveSet()
    flux = sp(wave)
    new_wave = N.compress(wave >= minw, wave)
    new_flux = N.compress(wave >= minw, flux)
    new_wave = N.compress(new_wave <= maxw, new_wave)
    new_flux = N.compress(new_wave <= maxw, new_flux)
    result = TabularSourceSpectrum()
    result._wavetable = new_wave
    result._fluxtable = new_flux
    result.waveunits = units.Units(sp.waveunits.name)
    result.fluxunits = units.Units(sp.fluxunits.name)
    return result