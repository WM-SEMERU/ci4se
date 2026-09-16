def set_device_scale(self, x_scale, y_scale):
    cairo.cairo_surface_set_device_scale(self._pointer, x_scale, y_scale)
    self._check_status()