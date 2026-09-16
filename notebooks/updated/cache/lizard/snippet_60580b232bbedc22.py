def fetchone(self):
    self._cursorLock.acquire()
    if self._currentBlock is not None and self._currentRecordNum < len(self
        ._currentBlock):
        x = self._currentRecordNum
        self._currentRecordNum += 1
        self._cursorLock.release()
        return self._currentBlock[x]
    if self._standbyBlock is None:
        self._fetchBlock()
    if self._standbyBlock is None or len(self._standbyBlock) == 0:
        self._cursorLock.release()
        return None
    self._currentBlock = self._standbyBlock
    self._standbyBlock = None
    self._currentRecordNum = 1
    self._cursorLock.release()
    return self._currentBlock[0]