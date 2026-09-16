def precipitable_water(self, value=999.0):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `precipitable_water`'
                .format(value))
    self._precipitable_water = value