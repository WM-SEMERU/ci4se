def post(self, json=None):
    return self._call('post', url=self.endpoint, json=json)