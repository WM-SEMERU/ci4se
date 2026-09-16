def _dpi(self, density):
    if self._density_units == 1:
        dpi = density
    elif self._density_units == 2:
        dpi = int(round(density * 2.54))
    else:
        dpi = 72
    return dpi