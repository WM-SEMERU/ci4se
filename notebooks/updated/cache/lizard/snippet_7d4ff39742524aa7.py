def get(self, thumbnail_name):
    if isinstance(thumbnail_name, list):
        thumbnail_name = '/'.join(thumbnail_name)
    return self._get(thumbnail_name)