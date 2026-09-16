def upload(self, resource_id, data):
    self.body = data
    self.content_type = 'application/octet-stream'
    self.resource_id(str(resource_id))
    self._request_uri = '{}/upload'.format(self._request_uri)