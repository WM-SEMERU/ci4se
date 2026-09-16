def parse(self, charset=None, headers=None):
    if headers:
        self.headers = headers
    else:
        if self.head:
            responses = self.head.rsplit(b'\nHTTP/', 1)
            _, response = responses[-1].split(b'\n', 1)
            response = response.decode('utf-8', 'ignore')
        else:
            response = ''
        if six.PY2:
            response = response.encode('utf-8')
        self.headers = email.message_from_string(response)
    if charset is None:
        if isinstance(self.body, six.text_type):
            self.charset = 'utf-8'
        else:
            self.detect_charset()
    else:
        self.charset = charset.lower()
    self._unicode_body = None