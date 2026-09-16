def id(self):
    if not self._id:
        self._id = tuple(sorted(map(str, self)))
    return self._id