def setDataFrame(self, dataFrame, copyDataFrame=False, filePath=None):
    if not isinstance(dataFrame, pandas.core.frame.DataFrame):
        raise TypeError('not of type pandas.core.frame.DataFrame')
    self.layoutAboutToBeChanged.emit()
    if copyDataFrame:
        self._dataFrame = dataFrame.copy()
    else:
        self._dataFrame = dataFrame
    self._columnDtypeModel = ColumnDtypeModel(dataFrame)
    self._columnDtypeModel.dtypeChanged.connect(self.propagateDtypeChanges)
    self._columnDtypeModel.changeFailed.connect(lambda columnName, index,
        dtype: self.changingDtypeFailed.emit(columnName, index, dtype))
    if filePath is not None:
        self._filePath = filePath
    self.layoutChanged.emit()
    self.dataChanged.emit()
    self.dataFrameChanged.emit()