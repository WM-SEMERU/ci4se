def _compensate_humidity(self, adc_h):
    var_h = self._temp_fine - 76800.0
    if var_h == 0:
        return 0
    var_h = (adc_h - (self._calibration_h[3] * 64.0 + self._calibration_h[4
        ] / 16384.0 * var_h)) * (self._calibration_h[1] / 65536.0 * (1.0 + 
        self._calibration_h[5] / 67108864.0 * var_h * (1.0 + self.
        _calibration_h[2] / 67108864.0 * var_h)))
    var_h *= 1.0 - self._calibration_h[0] * var_h / 524288.0
    if var_h > 100.0:
        var_h = 100.0
    elif var_h < 0.0:
        var_h = 0.0
    return var_h