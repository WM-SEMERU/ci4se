def checkValidCell(self, index):
    col = index.column()
    row = index.row()
    return self.model.isFieldValid(row, self._headers[index.column()])