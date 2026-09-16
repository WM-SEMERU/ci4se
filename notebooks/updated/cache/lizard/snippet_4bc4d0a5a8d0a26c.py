def get_color_stops(self):
    count = ffi.new('int *')
    _check_status(cairo.cairo_pattern_get_color_stop_count(self._pointer,
        count))
    stops = []
    stop = ffi.new('double[5]')
    for i in range(count[0]):
        _check_status(cairo.cairo_pattern_get_color_stop_rgba(self._pointer,
            i, stop + 0, stop + 1, stop + 2, stop + 3, stop + 4))
        stops.append(tuple(stop))
    return stops