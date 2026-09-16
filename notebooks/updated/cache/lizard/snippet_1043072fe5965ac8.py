def open(self, path, filename=None):
    scheme, key = self.getkey(path, filename=filename)
    return BotoReadFileHandle(scheme, key)