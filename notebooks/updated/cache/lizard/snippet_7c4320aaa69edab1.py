def update(self, data, timeout=-1, force=False):
    uri = self.data['uri']
    self.data = self._helper.update(data, uri=uri, timeout=timeout, force=force
        )
    return self