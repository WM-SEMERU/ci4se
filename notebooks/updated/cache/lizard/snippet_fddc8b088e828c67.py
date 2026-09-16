def fromSet(self, values):
    value = 0
    for flag in values:
        value |= self(flag)
    return value