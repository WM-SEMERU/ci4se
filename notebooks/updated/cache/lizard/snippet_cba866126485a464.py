def wd_db996(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `wd_db996`'.
                format(value))
    self._wd_db996 = value