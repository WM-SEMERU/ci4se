def transform(self, **kwds):
    result = self._client.photo.transform(self, **kwds)
    self._replace_fields(result.get_fields())