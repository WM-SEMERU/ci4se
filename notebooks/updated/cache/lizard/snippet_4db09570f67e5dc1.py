def setViewModel(self, model):
    if isinstance(model, DataFrameModel):
        self.enableEditing(False)
        self.uncheckButton()
        selectionModel = self.tableView.selectionModel()
        self.tableView.setModel(model)
        model.dtypeChanged.connect(self.updateDelegate)
        model.dataChanged.connect(self.updateDelegates)
        del selectionModel