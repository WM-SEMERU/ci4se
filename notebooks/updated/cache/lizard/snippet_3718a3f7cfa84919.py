def setHint(self, hint):
    if self.normalizePath():
        filepath = os.path.normpath(nativestring(hint))
    else:
        filepath = os.path.normpath(nativestring(hint)).replace('\\', '/')
    self._filepathEdit.setHint(hint)