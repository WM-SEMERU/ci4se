def _openFile(self):
    file_types = (
        'Comma Separated Values (*.csv);;Text files (*.txt);;All Files (*)')
    ret = QtGui.QFileDialog.getOpenFileName(self, self.tr('open file'),
        filter=file_types)
    if isinstance(ret, tuple):
        ret = ret[0]
    if ret:
        self._filenameLineEdit.setText(ret)
        self._updateFilename()