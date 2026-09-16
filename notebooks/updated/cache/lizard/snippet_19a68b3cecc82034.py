def en020(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `en020`'.
                format(value))
    self._en020 = value