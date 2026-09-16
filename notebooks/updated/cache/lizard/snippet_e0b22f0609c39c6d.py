def __shapeIndex(self, i=None):
    shx = self.shx
    if not shx:
        return None
    if not self._offsets:
        shx.seek(24)
        shxRecordLength = unpack('>i', shx.read(4))[0] * 2 - 100
        numRecords = shxRecordLength // 8
        shx.seek(100)
        for r in range(numRecords):
            self._offsets.append(unpack('>i', shx.read(4))[0] * 2)
            shx.seek(shx.tell() + 4)
    if not i == None:
        return self._offsets[i]