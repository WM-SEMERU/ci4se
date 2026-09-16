def saveFileEnc(self, filename, encoding):
    ret = libxml2mod.xmlSaveFileEnc(filename, self._o, encoding)
    return ret