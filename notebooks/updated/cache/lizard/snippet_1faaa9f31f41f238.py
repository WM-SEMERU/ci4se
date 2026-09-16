def default_start_index(self, value):
    if not isinstance(value, int):
        raise TypeError('default_start_index attribute must be of int type.')
    self._default_start_index = value