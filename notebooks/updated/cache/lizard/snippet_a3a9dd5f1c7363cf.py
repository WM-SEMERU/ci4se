def loadFile(self, fileName):
    self.fileName = fileName
    self.file = QtCore.QFile(fileName)
    if self.file.exists():
        self.qteScintilla.setText(open(fileName).read())
        self.qteScintilla.qteUndoStack.reset()
    else:
        msg = 'File <b>{}</b> does not exist'.format(self.qteAppletID())
        self.qteLogger.info(msg)