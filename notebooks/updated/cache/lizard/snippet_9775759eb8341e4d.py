def delete(self):
    resp = self._client.delete(type(self).api_endpoint, model=self)
    if 'error' in resp:
        return False
    self.invalidate()
    return True