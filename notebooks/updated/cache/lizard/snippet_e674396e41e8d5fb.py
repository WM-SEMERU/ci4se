def convert_values(self):

    def stringify(value):
        if self.encoding is not None:
            encoder = partial(pprint_thing_encoded, encoding=self.encoding)
        else:
            encoder = pprint_thing
        return encoder(value)
    lhs, rhs = self.lhs, self.rhs
    if is_term(lhs) and lhs.is_datetime and is_term(rhs) and rhs.is_scalar:
        v = rhs.value
        if isinstance(v, (int, float)):
            v = stringify(v)
        v = Timestamp(_ensure_decoded(v))
        if v.tz is not None:
            v = v.tz_convert('UTC')
        self.rhs.update(v)
    if is_term(rhs) and rhs.is_datetime and is_term(lhs) and lhs.is_scalar:
        v = lhs.value
        if isinstance(v, (int, float)):
            v = stringify(v)
        v = Timestamp(_ensure_decoded(v))
        if v.tz is not None:
            v = v.tz_convert('UTC')
        self.lhs.update(v)