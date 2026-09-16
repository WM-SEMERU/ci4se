def set(self, key, value):
    url = self._url('{}'.format(key))
    body = {'value': value}
    return self.client.put(url, data=body)