def setTopLevelItems(self, items):
    self.blockSignals(True)
    root = self.invisibleRootItem()
    for row in range(root.rowCount()):
        root.takeRow(row)
    for item in items:
        root.appendRow(item)
    self.blockSignals(False)