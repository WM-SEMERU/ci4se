def insertFromMimeData(self, data):
    undoObj = UndoPaste(self, data, self.pasteCnt)
    self.pasteCnt += 1
    self.qteUndoStack.push(undoObj)