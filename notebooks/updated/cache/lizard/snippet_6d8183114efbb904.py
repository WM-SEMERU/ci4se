def depth_april_average_ground_temperature(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `depth_april_average_ground_temperature`'
                .format(value))
    self._depth_april_average_ground_temperature = value