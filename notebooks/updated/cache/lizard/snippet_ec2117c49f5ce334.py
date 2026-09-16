def plot(self, wavelengths=None, **kwargs):
    w, y = self._get_arrays(wavelengths)
    self._do_plot(w, y, **kwargs)