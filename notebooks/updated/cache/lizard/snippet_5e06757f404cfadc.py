def clearAndSetComboBoxes(self, axesNames):
    logger.debug('Collector clearAndSetComboBoxes: {}'.format(axesNames))
    check_is_a_sequence(axesNames)
    row = 0
    self._deleteComboBoxes(row)
    self.clear()
    self._setAxesNames(axesNames)
    self._createComboBoxes(row)
    self._updateWidgets()