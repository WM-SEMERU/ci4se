def integrate(self, wavelengths=None, **kwargs):
    if 'flux_unit' in kwargs:
        self._validate_flux_unit(kwargs['flux_unit'], wav_only=True)
    x = self._validate_wavelengths(wavelengths)
    try:
        m = self.model.integral
    except (AttributeError, NotImplementedError):
        if conf.default_integrator == 'trapezoid':
            y = self(x, **kwargs)
            result = abs(np.trapz(y.value, x=x.value))
            result_unit = y.unit
        else:
            raise NotImplementedError(
                'Analytic integral not available and default integrator {0} is not supported'
                .format(conf.default_integrator))
    else:
        start = x[0].value
        stop = x[-1].value
        result = m(stop) - m(start)
        result_unit = self._internal_flux_unit
    if result_unit != units.THROUGHPUT:
        if result_unit == units.PHOTLAM:
            result_unit = u.photon / (u.cm ** 2 * u.s)
        elif result_unit == units.FLAM:
            result_unit = u.erg / (u.cm ** 2 * u.s)
        else:
            raise NotImplementedError('Integration of {0} is not supported'
                .format(result_unit))
    else:
        result_unit *= self._internal_wave_unit
    return result * result_unit