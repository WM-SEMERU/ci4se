def is_convertible_with(self, other):
    other = as_dimension(other)
    return (self._value is None or other.value is None or self._value ==
        other.value)