def setMode(self, mode):
    self.mode = mode
    if mode == BuildMode:
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.setSelectionModel(QtGui.QItemSelectionModel(self.model()))
        self.setEnabled(True)
        self.model().updateComponentStartVals()
    else:
        self.model().purgeAutoSelected()
        self.setSelectionModel(ComponentSelectionModel(self.model()))
        self.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)