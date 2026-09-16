def headerData(self, section, orientation, role):
    if orientation == QtCore.Qt.Horizontal:
        d = self._root.data(section, role)
        if d is None and role == QtCore.Qt.DisplayRole:
            return str(section + 1)
        return d
    if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
        return str(section + 1)