def plot(self, wavelengths=None, flux_unit=None, area=None, vegaspec=None,
    **kwargs):
    w, y = self._get_arrays(wavelengths, flux_unit=flux_unit, area=area,
        vegaspec=vegaspec)
    self._do_plot(w, y, **kwargs)