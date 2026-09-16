def ping(self):
    uri = '%s/%s' % (self.base_uri, 'ping')
    resp, data = self.request('GET', uri)
    return data