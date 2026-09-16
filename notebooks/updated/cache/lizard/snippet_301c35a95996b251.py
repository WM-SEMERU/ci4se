def unkown_field(self, value=None):
    if value is not None:
        try:
            value = str(value)
        except ValueError:
            raise ValueError(
                'value {} need to be of type str for field `unkown_field`'.
                format(value))
        if ',' in value:
            raise ValueError(
                'value should not contain a comma for field `unkown_field`')
    self._unkown_field = value