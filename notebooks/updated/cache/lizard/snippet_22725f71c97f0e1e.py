def set_ramp_rate(self, ramp_rate):
    set_cmd = self._create_set_property_msg('_ramp_rate', 5, ramp_rate)
    self._send_method(set_cmd, self._property_set)