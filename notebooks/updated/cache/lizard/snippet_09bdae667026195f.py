def createConnection(self):
    readerobj = None
    if isinstance(self.reader, Reader):
        readerobj = self.reader
    elif type(self.reader) == str:
        for reader in readers():
            if self.reader == str(reader):
                readerobj = reader
    if readerobj:
        return readerobj.createConnection()
    else:
        return None