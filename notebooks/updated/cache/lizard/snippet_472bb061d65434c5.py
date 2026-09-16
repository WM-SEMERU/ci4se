def row_major(self, value):
    if value is not None:
        if not isinstance(value, bool):
            raise TypeError('f90nml: error: row_major must be a logical value.'
                )
        else:
            self._row_major = value