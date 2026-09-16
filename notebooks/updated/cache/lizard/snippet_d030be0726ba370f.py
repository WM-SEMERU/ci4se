def break_name(self, break_name):
    if break_name is None:
        raise ValueError('Invalid value for `break_name`, must not be `None`')
    if len(break_name) < 1:
        raise ValueError(
            'Invalid value for `break_name`, length must be greater than or equal to `1`'
            )
    self._break_name = break_name