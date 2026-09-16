def direction(self, direction):
    if not isinstance(direction, str):
        raise TypeError('direction must be of type str')
    accepted_values = ['i', 'x', 'y', 'z', 's', 'c']
    if direction not in accepted_values:
        raise ValueError('must be one of: {}'.format(accepted_values))
    self._direction = direction