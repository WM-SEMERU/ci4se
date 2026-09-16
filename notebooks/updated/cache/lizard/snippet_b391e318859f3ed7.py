def removeComponent(self, row, col):
    self._segments[row].pop(col)
    if self.columnCountForRow(-1) == 0:
        self.removeRow(len(self._segments) - 1)
    self.updateCalibration()