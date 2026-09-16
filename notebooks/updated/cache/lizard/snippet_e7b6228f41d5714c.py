def pause(self, container):
    url = self._url('/containers/{0}/pause', container)
    res = self._post(url)
    self._raise_for_status(res)