def get_time_position(self, time):
    if time < self._start or time > self._finish:
        raise ValueError('time argument out of bounds')
    return (time - self._start) / (self._resolution / self._zoom_factor)