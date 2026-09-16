def bind(self):
    self._COOKIES = None
    self.status = 200
    self.headers = HeaderDict()
    self.content_type = 'text/html; charset=UTF-8'