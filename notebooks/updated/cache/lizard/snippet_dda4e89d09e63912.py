def value(self):
    if self.isenum():
        if isinstance(self._value, self.enum_ref):
            return self._value.value
        return self._value
    elif self.is_bitmask():
        return self._value.bitmask
    else:
        return self._value