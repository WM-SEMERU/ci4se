def filepaths(self):
    return nativestring(self._filepathEdit.text()).split(os.path.pathsep)