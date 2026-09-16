def max_width(self):
    value, unit = float(self._width_str[:-1]), self._width_str[-1]
    ensure(unit in ['c', '%'], ValueError,
        "Width unit must be either 'c' or '%'")
    if unit == 'c':
        ensure(value <= self.columns, ValueError,
            'Terminal only has {} columns, cannot draw bar of size {}.'.
            format(self.columns, value))
        retval = value
    else:
        ensure(0 < value <= 100, ValueError,
            'value=={} does not satisfy 0 < value <= 100'.format(value))
        dec = value / 100
        retval = dec * self.columns
    return floor(retval)