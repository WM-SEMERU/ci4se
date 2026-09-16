def writeMixedArray(self, o):
    if self.writeReference(o) != -1:
        return
    self.context.addObject(o)
    self.writeType(TYPE_MIXEDARRAY)
    try:
        max_index = max([y[0] for y in o.items() if isinstance(y[0], (int,
            long))])
        if max_index < 0:
            max_index = 0
    except ValueError:
        max_index = 0
    self.stream.write_ulong(max_index)
    self._writeDict(o)
    self._writeEndObject()