def on_tblFunctions1_itemSelectionChanged(self):
    self.parent.step_fc_functions2.tblFunctions2.clearContents()
    self.parent.step_fc_functions2.lblAvailableFunctions2.clear()
    self.parent.pbnNext.setEnabled(True)
    selection = self.tblFunctions1.selectedItems()
    selItem = len(selection) == 1 and selection[0] or None
    for row in range(self.tblFunctions1.rowCount()):
        for column in range(self.tblFunctions1.columnCount()):
            item = self.tblFunctions1.item(row, column)
            item.setText(item == selItem and '•' or '')