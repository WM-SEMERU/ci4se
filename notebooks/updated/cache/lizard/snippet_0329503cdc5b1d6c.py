def call(self, **data):
    uri, body, headers = self.prepare(data)
    return self.dispatch(uri, body, headers)