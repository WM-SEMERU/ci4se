def _imshow_array2d(self, array, origin='lower', interpolation='none',
    aspect='auto', **kwargs):
    extent = tuple(array.xspan) + tuple(array.yspan)
    if self.get_xscale() == 'log' and extent[0] == 0.0:
        extent = (1e-300,) + extent[1:]
    if self.get_yscale() == 'log' and extent[2] == 0.0:
        extent = extent[:2] + (1e-300,) + extent[3:]
    kwargs.setdefault('extent', extent)
    return self.imshow(array.value.T, origin=origin, aspect=aspect,
        interpolation=interpolation, **kwargs)