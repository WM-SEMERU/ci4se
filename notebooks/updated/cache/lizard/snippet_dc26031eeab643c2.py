def replace(self, photo_file, **kwds):
    result = self._client.photo.replace(self, photo_file, **kwds)
    self._replace_fields(result.get_fields())