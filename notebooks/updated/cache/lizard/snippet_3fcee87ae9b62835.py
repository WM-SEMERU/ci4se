def speed_d(self):
    self._speed_d, value = self.get_attr_int(self._speed_d, 'speed_pid/Kd')
    return value