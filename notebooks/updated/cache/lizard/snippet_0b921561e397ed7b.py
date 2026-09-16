def fromMimeData(self, data):
    if data.hasText():
        self.insert(data.text())
    return QtCore.QByteArray(), False