def readString(self):
    length, is_reference = self._readLength()
    if is_reference:
        result = self.context.getString(length)
        return self.context.getStringForBytes(result)
    if length == 0:
        return ''
    result = self.stream.read(length)
    self.context.addString(result)
    return self.context.getStringForBytes(result)