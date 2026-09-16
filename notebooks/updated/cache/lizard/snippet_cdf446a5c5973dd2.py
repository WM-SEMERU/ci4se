def append(self, text: str):
    pos = self.getCursorPosition()
    line, col = self.getNumLinesAndColumns()
    undoObj = UndoInsertAt(self, text, line, col)
    self.qteUndoStack.push(undoObj)
    self.setCursorPosition(*pos)