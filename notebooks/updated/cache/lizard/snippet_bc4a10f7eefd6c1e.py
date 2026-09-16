def embeddedFileAdd(self, buffer, name, filename=None, ufilename=None, desc
    =None):
    if self.isClosed or self.isEncrypted:
        raise ValueError('operation illegal for closed / encrypted doc')
    return _fitz.Document_embeddedFileAdd(self, buffer, name, filename,
        ufilename, desc)