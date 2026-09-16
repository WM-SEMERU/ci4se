def rename(self, container, name):
    url = self._url('/containers/{0}/rename', container)
    params = {'name': name}
    res = self._post(url, params=params)
    self._raise_for_status(res)