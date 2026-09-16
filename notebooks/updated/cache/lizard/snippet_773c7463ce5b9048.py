def db990(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `db990`'.
                format(value))
    self._db990 = value