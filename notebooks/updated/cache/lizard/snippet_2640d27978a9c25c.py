def _FindFileContainingSymbolInDb(self, symbol):
    try:
        file_proto = self._internal_db.FindFileContainingSymbol(symbol)
    except KeyError as error:
        if self._descriptor_db:
            file_proto = self._descriptor_db.FindFileContainingSymbol(symbol)
        else:
            raise error
    if not file_proto:
        raise KeyError('Cannot find a file containing %s' % symbol)
    return self._ConvertFileProtoToFileDescriptor(file_proto)