def _getPageObjNumber(self, pno):
    if self.isClosed:
        raise ValueError('operation illegal for closed doc')
    return _fitz.Document__getPageObjNumber(self, pno)