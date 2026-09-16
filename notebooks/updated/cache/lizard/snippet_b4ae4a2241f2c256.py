def _iterateDocumentCharsForward(self, block, startColumnIndex):
    endTime = time.time() + self._MAX_SEARCH_TIME_SEC
    for columnIndex, char in list(enumerate(block.text()))[startColumnIndex:]:
        yield block, columnIndex, char
    block = block.next()
    while block.isValid():
        for columnIndex, char in enumerate(block.text()):
            yield block, columnIndex, char
        if time.time() > endTime:
            raise _TimeoutException('Time is over')
        block = block.next()