def createFile(self, fileName, desiredAccess, shareMode,
    creationDisposition, flagsAndAttributes, dokanFileInfo):
    return self.operations('createFile', fileName)