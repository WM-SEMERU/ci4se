def absolute_magnitude(self, richness=1, steps=10000.0):
    params = {k: v.value for k, v in self._params.items()}
    params.update(band_1='g', band_2='r', survey='sdss')
    iso = self.__class__(**params)
    mass_init, mass_pdf, mass_act, sdss_g, sdss_r = iso.sample(mass_steps=steps
        )
    V = jester_mag_v(sdss_g, sdss_r)
    return sum_mags(V, weights=mass_pdf * richness)