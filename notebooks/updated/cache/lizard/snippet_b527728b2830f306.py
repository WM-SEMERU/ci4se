def rgb(self):
    coords = tuple(self.dimension_values(d, expanded=False) for d in self.kdims
        )
    data = [self.dimension_values(d, flat=False) for d in self.vdims]
    hsv = self.hsv_to_rgb(*data[:3])
    if len(self.vdims) == 4:
        hsv += data[3],
    params = util.get_param_values(self)
    del params['vdims']
    return RGB(coords + hsv, bounds=self.bounds, xdensity=self.xdensity,
        ydensity=self.ydensity, **params)