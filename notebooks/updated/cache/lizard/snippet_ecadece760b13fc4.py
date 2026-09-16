def unpack(self, buff, offset=0):
    try:
        self._value = struct.unpack_from(self._fmt, buff, offset)[0]
        if self.enum_ref:
            self._value = self.enum_ref(self._value)
    except (struct.error, TypeError, ValueError) as exception:
        msg = '{}; fmt = {}, buff = {}, offset = {}.'.format(exception,
            self._fmt, buff, offset)
        raise UnpackException(msg)