def update(self, resource, timeout=-1):
    return self._client.update(resource, timeout=timeout, default_values=
        self.DEFAULT_VALUES, uri=self.URI)