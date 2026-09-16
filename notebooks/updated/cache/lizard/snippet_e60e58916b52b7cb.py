def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
    self.beginRemoveRows(parent, position, position + rows - 1)
    for i in range(rows):
        self.model.removeRow(position)
    self.endRemoveRows()
    if self.rowCount() == 0:
        self.emptied.emit(True)
    return True