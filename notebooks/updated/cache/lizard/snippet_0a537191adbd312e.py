def getPageFontList(self, pno):
    if self.isClosed or self.isEncrypted:
        raise ValueError('operation illegal for closed / encrypted doc')
    if self.isPDF:
        return self._getPageInfo(pno, 1)
    return []