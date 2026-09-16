def ground_temperature_depth(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `ground_temperature_depth`'
                .format(value))
    self._ground_temperature_depth = value