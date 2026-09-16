def login(self, username, json_document):
    url = '{}u/{}'.format(self.url, username)
    make_request(url, method='PUT', body=json_document, timeout=self.timeout)