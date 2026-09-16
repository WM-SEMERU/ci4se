def _readMultiple(self, start, end, db):
    self._validatePos(start, end)
    return [bytes(db.get(str(pos))) for pos in range(start, end + 1)]