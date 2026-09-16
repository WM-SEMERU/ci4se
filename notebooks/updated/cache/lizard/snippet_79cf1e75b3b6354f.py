def magnitude2cps(self, magnitude):
    cps = data_util.magnitude2cps(magnitude, magnitude_zero_point=self.
        _magnitude_zero_point)
    if self._data_count_unit == 'e-':
        cps *= self.ccd_gain
    return cps