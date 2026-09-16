def create_pgroup_snapshots(self, sources, **kwargs):
    data = {'source': sources, 'snap': True}
    data.update(kwargs)
    return self._request('POST', 'pgroup', data)