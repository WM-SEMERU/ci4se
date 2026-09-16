def rfile(self):
    self.__class__ = File
    self._morph()
    self.clear()
    return File.rfile(self)