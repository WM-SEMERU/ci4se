def save(self, filename, garbage=0, clean=0, deflate=0, incremental=0,
    ascii=0, expand=0, linear=0, pretty=0, decrypt=1):
    if self.isClosed or self.isEncrypted:
        raise ValueError('operation illegal for closed / encrypted doc')
    if type(filename) == str:
        pass
    elif type(filename) == unicode:
        filename = filename.encode('utf8')
    else:
        raise TypeError('filename must be a string')
    if filename == self.name and not incremental:
        raise ValueError('save to original must be incremental')
    if self.pageCount < 1:
        raise ValueError('cannot save with zero pages')
    if incremental:
        if self.name != filename or self.stream:
            raise ValueError('incremental needs original file')
    return _fitz.Document_save(self, filename, garbage, clean, deflate,
        incremental, ascii, expand, linear, pretty, decrypt)