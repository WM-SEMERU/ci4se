def putkeyword(self, keyword, value, makesubrecord=False):
    return self._table.putcolkeyword(self._column, keyword, value,
        makesubrecord)