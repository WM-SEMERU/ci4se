def commit(self, f):
    if self._overwrite:
        replace_atomic(f.name, self._path)
    else:
        move_atomic(f.name, self._path)