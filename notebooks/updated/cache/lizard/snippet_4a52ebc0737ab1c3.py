def _get_line(self):
    line = self._f.readline()
    if len(line) == 0:
        raise StopIteration
    return line