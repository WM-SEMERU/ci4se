def rsub(self, other, axis='columns', level=None, fill_value=None):
    return self._binary_op('rsub', other, axis=axis, level=level,
        fill_value=fill_value)