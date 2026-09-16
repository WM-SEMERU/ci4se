def writeFile(self, fileName, buffer, numberOfBytesToWrite,
    numberOfBytesWritten, offset, dokanFileInfo):
    return self.operations('writeFile', fileName, buffer,
        numberOfBytesToWrite, offset)