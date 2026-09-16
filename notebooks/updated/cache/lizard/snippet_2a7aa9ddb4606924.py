def wmo(self, value=None):
    if value is not None:
        try:
            value = str(value)
        except ValueError:
            raise ValueError('value {} need to be of type str for field `wmo`'
                .format(value))
        if ',' in value:
            raise ValueError('value should not contain a comma for field `wmo`'
                )
    self._wmo = value