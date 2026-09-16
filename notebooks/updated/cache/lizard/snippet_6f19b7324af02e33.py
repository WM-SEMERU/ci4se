def fan_speed(self, value):
    if value not in range(1, 10):
        raise exceptions.RoasterValueError
    self._fan_speed.value = value