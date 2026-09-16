def inspect_secret(self, id):
    url = self._url('/secrets/{0}', id)
    return self._result(self._get(url), True)