def _set_pwm(self, raw_values):
    for i in range(len(self._pins)):
        self._device.set_pwm(self._pins[i], 0, raw_values[i])