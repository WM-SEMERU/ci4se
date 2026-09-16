def getSlicesString(self):
    if not self.rtiIsSliceable:
        return ''
    nDims = self.rti.nDims
    sliceList = [':'] * nDims
    for spinBox in self._spinBoxes:
        dimNr = spinBox.property('dim_nr')
        sliceList[dimNr] = str(spinBox.value())
    return '[' + ', '.join(sliceList) + ']'