def as_posix(self):
    f = self._flavour
    return str(self).replace(f.sep, '/')