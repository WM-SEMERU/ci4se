def to_pixel(self, wcs, mode='all'):
    pixel_params = self._to_pixel_params(wcs, mode=mode)
    return RectangularAperture(**pixel_params)