def _set_names(self, values, level=None):
    if not is_list_like(values):
        raise ValueError('Names must be a list-like')
    if len(values) != 1:
        raise ValueError('Length of new names must be 1, got %d' % len(values))
    for name in values:
        if not is_hashable(name):
            raise TypeError('{}.name must be a hashable type'.format(self.
                __class__.__name__))
    self.name = values[0]