def _updateObject(self, xref, text, page=None):
    if self.isClosed or self.isEncrypted:
        raise ValueError('operation illegal for closed / encrypted doc')
    return _fitz.Document__updateObject(self, xref, text, page)