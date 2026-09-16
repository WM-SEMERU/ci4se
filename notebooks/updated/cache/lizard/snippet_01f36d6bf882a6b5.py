def set_data(self, column, value, role):
    if role == QtCore.Qt.EditRole or role == QtCore.Qt.DisplayRole:
        self._list[column] = value
        return True
    else:
        return False