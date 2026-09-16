def reload(self):
    result = self._client._get(self.__class__.base_url(self.sys['id']))
    self._update_from_resource(result)
    return self