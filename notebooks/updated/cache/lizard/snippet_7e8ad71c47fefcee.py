def _updateRtiInfo(self):
    logger.debug('Updating self._rtiInfo')
    rti = self.rti
    if rti is None:
        info = {'slices': '', 'name': '', 'path': '', 'file-name': '',
            'dir-name': '', 'base-name': '', 'unit': '', 'raw-unit': ''}
    else:
        dirName, baseName = os.path.split(rti.fileName)
        info = {'slices': self.getSlicesString(), 'name': rti.nodeName,
            'path': rti.nodePath, 'file-name': rti.fileName, 'dir-name':
            dirName, 'base-name': baseName, 'unit': '({})'.format(rti.unit) if
            rti.unit else '', 'raw-unit': rti.unit}
    for axisName, comboBox in zip(self._axisNames, self._comboBoxes):
        dimName = comboBox.currentText()
        key = '{}-dim'.format(axisName.lower())
        info[key] = dimName
    self._rtiInfo = info