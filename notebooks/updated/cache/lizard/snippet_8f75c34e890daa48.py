def _to_temperature(self, temperature):
    self._to_value(self._temperature, temperature, self.command_set.
        temperature_steps, self._warmer, self._cooler)