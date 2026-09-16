def dp010(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `dp010`'.
                format(value))
    self._dp010 = value