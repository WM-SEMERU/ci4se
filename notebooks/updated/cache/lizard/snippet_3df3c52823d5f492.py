def connect_hgroup(self, hgroup, volume, **kwargs):
    return self._request('POST', 'hgroup/{0}/volume/{1}'.format(hgroup,
        volume), kwargs)