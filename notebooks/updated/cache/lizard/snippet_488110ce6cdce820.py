def _populateComboBoxes(self, row):
    logger.debug('_populateComboBoxes')
    for comboBox in self._comboBoxes:
        comboBox.clear()
    if not self.rtiIsSliceable:
        for comboBoxNr, comboBox in enumerate(self._comboBoxes):
            comboBox.addItem('', userData=None)
            comboBox.setEnabled(False)
        return
    nDims = self._rti.nDims
    nCombos = len(self._comboBoxes)
    for comboBoxNr, comboBox in enumerate(self._comboBoxes):
        comboBox.addItem(FAKE_DIM_NAME, userData=FAKE_DIM_OFFSET + comboBoxNr)
        for dimNr in range(nDims):
            comboBox.addItem(self._rti.dimensionNames[dimNr], userData=dimNr)
        if nDims >= nCombos:
            curIdx = nDims + 1 - nCombos + comboBoxNr
        else:
            curIdx = comboBoxNr + 1 if comboBoxNr < nDims else 0
        assert 0 <= curIdx <= nDims + 1, 'curIdx should be <= {}, got {}'.format(
            nDims + 1, curIdx)
        comboBox.setCurrentIndex(curIdx)
        comboBox.setEnabled(True)