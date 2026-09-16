def update(self, attributes=None):
    if attributes is None:
        attributes = {}
    headers = self.__class__.create_headers(attributes)
    headers.update(self._update_headers())
    result = self._client._put(self._update_url(), self.__class__.
        create_attributes(attributes, self), headers=headers)
    self._update_from_resource(result)
    return self