def write(self, filename, header=None):
    origfile = self._filename
    try:
        with open(filename, 'w') as _file:
            self.writestream(_file, header)
            self._filename = filename
        return True
    except IOError:
        self._filename = origfile
        return False