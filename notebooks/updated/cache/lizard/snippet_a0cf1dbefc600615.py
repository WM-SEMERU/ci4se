def Entry(self, name, directory=None, create=1):
    return self._lookup(name, directory, Entry, create)