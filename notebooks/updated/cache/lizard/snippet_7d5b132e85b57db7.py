def ws025(self, value=None):
    if value is not None:
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type float for field `ws025`'.
                format(value))
    self._ws025 = value