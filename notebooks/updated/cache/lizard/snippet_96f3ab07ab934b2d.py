def set_series_capacitance(self, channel, value, resistor_index=None):
    if resistor_index is None:
        resistor_index = self.series_resistor_index(channel)
    try:
        if channel == 0:
            self.calibration.C_hv[resistor_index] = value
        else:
            self.calibration.C_fb[resistor_index] = value
    except:
        pass
    return self._set_series_capacitance(channel, value)