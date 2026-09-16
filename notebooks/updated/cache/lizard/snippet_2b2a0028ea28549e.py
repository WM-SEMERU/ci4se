def dew_point_temperature(self, value=99.9):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `dew_point_temperature`'
                .format(value))
        if value <= -70.0:
            raise ValueError(
                'value need to be greater -70.0 for field `dew_point_temperature`'
                )
        if value >= 70.0:
            raise ValueError(
                'value need to be smaller 70.0 for field `dew_point_temperature`'
                )
    self._dew_point_temperature = value