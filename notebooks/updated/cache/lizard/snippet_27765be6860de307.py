def removekeyword(self, keyword):
    if isinstance(keyword, str):
        self._removekeyword('', keyword, -1)
    else:
        self._removekeyword('', '', keyword)