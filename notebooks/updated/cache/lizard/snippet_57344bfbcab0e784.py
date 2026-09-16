def _pfp__set_value(self, new_val):
    if self._pfp__frozen:
        raise errors.UnmodifiableConst()
    if isinstance(new_val, IntBase):
        raw = new_val._pfp__build()
        while len(raw) < self.width:
            if self.endian == BIG_ENDIAN:
                raw = b'\x00' + raw
            else:
                raw += b'\x00'
        while len(raw) > self.width:
            if self.endian == BIG_ENDIAN:
                raw = raw[1:]
            else:
                raw = raw[:-1]
        self._pfp__parse(six.BytesIO(raw))
    else:
        mask = 1 << 8 * self.width
        if self.signed:
            max_val = mask // 2 - 1
            min_val = -(mask // 2)
        else:
            max_val = mask - 1
            min_val = 0
        if new_val < min_val:
            new_val += -min_val
            new_val &= mask - 1
            new_val -= -min_val
        elif new_val > max_val:
            new_val &= mask - 1
        self._pfp__value = new_val
    self._pfp__notify_parent()