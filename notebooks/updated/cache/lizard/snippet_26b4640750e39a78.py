def set_precision(self, width):
    if not type(width) is int or width < 0:
        raise ValueError('width must be an integer greater then 0')
    self._precision = width
    return self