def getSlicedArray(self, copy=True):
    if not self.rtiIsSliceable:
        return None
    nDims = self.rti.nDims
    sliceList = [slice(None)] * nDims
    for spinBox in self._spinBoxes:
        dimNr = spinBox.property('dim_nr')
        sliceList[dimNr] = spinBox.value()
    logger.debug('Array slice list: {}'.format(str(sliceList)))
    slicedArray = self.rti[tuple(sliceList)]
    if copy:
        slicedArray = ma.copy(slicedArray)
    if self.maxCombos == 0:
        slicedArray = ma.MaskedArray(slicedArray)
    check_is_an_array(slicedArray, np.ndarray)
    if not isinstance(slicedArray, ma.MaskedArray):
        slicedArray = ma.MaskedArray(slicedArray)
    for dimNr in range(slicedArray.ndim, self.maxCombos):
        slicedArray = ma.expand_dims(slicedArray, dimNr)
    assert slicedArray.ndim == self.maxCombos, 'Bug: getSlicedArray should return a {:d}D array, got: {}D'.format(
        self.maxCombos, slicedArray.ndim)
    awm = ArrayWithMask.createFromMaskedArray(slicedArray)
    del slicedArray
    comboDims = [self._comboBoxDimensionIndex(cb) for cb in self._comboBoxes]
    permutations = np.argsort(comboDims)
    logger.debug('slicedArray.shape: {}'.format(awm.data.shape))
    logger.debug('Transposing dimensions: {}'.format(permutations))
    awm = awm.transpose(permutations)
    awm.checkIsConsistent()
    return awm