def _Open(self):
    self._connection = sqlite3.connect(self._path, detect_types=sqlite3.
        PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    self._cursor = self._connection.cursor()