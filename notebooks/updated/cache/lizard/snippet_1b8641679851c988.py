def _post(self, url, params, uploads=None):
    self._call(self.POST, url, params, uploads)