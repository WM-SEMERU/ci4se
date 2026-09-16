def create(self, resource, timeout=-1):
    data = self.__default_values.copy()
    data.update(resource)
    return self._client.create(data, timeout=timeout)