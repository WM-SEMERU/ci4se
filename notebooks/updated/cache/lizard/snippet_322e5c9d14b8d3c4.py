def showRemoveColumnDialog(self, triggered):
    if triggered:
        model = self.tableView.model()
        if model is not None:
            columns = model.dataFrameColumns()
            dialog = RemoveAttributesDialog(columns, self)
            dialog.accepted.connect(self.removeColumns)
            dialog.rejected.connect(self.uncheckButton)
            dialog.show()