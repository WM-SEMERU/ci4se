def parse_value(self, value):
    parsed = super(IntField, self).parse_value(value)
    if parsed is None:
        return parsed
    return int(parsed)