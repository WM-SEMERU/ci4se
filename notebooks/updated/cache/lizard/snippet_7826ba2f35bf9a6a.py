def move_version(self, id, after=None, position=None):
    data = {}
    if after is not None:
        data['after'] = after
    elif position is not None:
        data['position'] = position
    url = self._get_url('version/' + id + '/move')
    r = self._session.post(url, data=json.dumps(data))
    version = Version(self._options, self._session, raw=json_loads(r))
    return version