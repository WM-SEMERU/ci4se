def useragent(self, value):
    if value is None:
        self._useragent = (
            'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
            )
    elif self._useragent != value:
        self._useragent = value