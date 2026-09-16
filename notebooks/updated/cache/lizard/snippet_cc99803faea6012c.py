def version(self, id, expand=None):
    version = Version(self._options, self._session)
    params = {}
    if expand is not None:
        params['expand'] = expand
    version.find(id, params=params)
    return version