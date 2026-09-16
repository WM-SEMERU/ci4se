def get_linear_points(self):
    points = ffi.new('double[4]')
    _check_status(cairo.cairo_pattern_get_linear_points(self._pointer, 
        points + 0, points + 1, points + 2, points + 3))
    return tuple(points)