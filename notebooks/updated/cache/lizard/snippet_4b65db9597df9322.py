def ramp_down_sp(self):
    self._ramp_down_sp, value = self.get_attr_int(self._ramp_down_sp,
        'ramp_down_sp')
    return value