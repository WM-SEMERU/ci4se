def setData(self, index, value, role):
    row = index.row()
    name, state = self.row(row)
    if role == Qt.CheckStateRole:
        self.set_row(row, [name, not state])
        self._parent.setCurrentIndex(index)
        self._parent.setFocus()
        self.dataChanged.emit(index, index)
        return True
    elif role == Qt.EditRole:
        self.set_row(row, [from_qvariant(value, to_text_string), state])
        self.dataChanged.emit(index, index)
        return True
    return True