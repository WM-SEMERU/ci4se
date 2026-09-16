def ParseFromHumanReadable(self, string):
    if not string:
        return None
    match = self.REGEX.match(string.strip().lower())
    if not match:
        raise DecodeError('Unknown specification for ByteSize %s' % string)
    multiplier = self.DIVIDERS.get(match.group(2))
    if not multiplier:
        raise DecodeError('Invalid multiplier %s' % match.group(2))
    value = match.group(1)
    if '.' in value:
        value = float(value)
    else:
        value = int(value)
    self._value = int(value * multiplier)