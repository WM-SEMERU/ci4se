def search(self, response_format=None, key=None, **kwargs):
    if response_format is None:
        response_format = self.response_format
    if key is None:
        key = self.key
    url = '%s%s?%sapi-key=%s' % (API_ROOT, response_format, self._options(
        **kwargs), key)
    r = requests.get(url)
    return r.json()