def set_size(self, size):
    if size == 'small':
        self._set_size_small()
    elif size == 'large':
        self._set_size_large()
    else:
        raise ValueError('Size must be large or small')