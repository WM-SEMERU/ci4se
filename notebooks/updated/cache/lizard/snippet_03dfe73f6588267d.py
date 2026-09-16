def previous_row(self):
    row = self.currentIndex().row()
    rows = self.proxy_model.rowCount()
    if row == 0:
        row = rows
    self.selectRow(row - 1)