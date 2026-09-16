def taskfileinfo_descriptor_data(tfi, role):
    if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
        return tfi.descriptor