def _readfile(self, filename):
    f = open(filename)
    self.content = f.readlines()
    f.close()