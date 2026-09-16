def get_position_time(self, position):
    return self._start + position * (self._resolution / self._zoom_factor)