def setExtension(self, ext):
    if ext[0] != '.':
        ext = '.' + ext
    self._ext = utils.asString(ext)