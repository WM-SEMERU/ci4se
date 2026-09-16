def setFilepathModeText(self, text):
    try:
        self.setFilepathMode(XFilepathEdit.Mode[nativestring(text)])
        return True
    except KeyError:
        return False