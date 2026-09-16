def do(self):
    data = None
    if self.body is not None and self.body != b'':
        data = self.body
    return requests.request(self.method, str(self.url), data=data, headers=
        self.header)