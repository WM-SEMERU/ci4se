def delete(self):
    if self._writeable:
        self._write(('CRVDEL', Integer), self.idx)
    else:
        raise RuntimeError('Can not delete read-only curves.')