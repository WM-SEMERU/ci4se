def convert(self, value, view):
    if isinstance(value, NUMERIC_TYPES):
        return value
    else:
        self.fail('must be numeric, not {0}'.format(type(value).__name__),
            view, True)