def send_pgroup_snapshot(self, source, **kwargs):
    data = {'name': [source], 'action': 'send'}
    data.update(kwargs)
    return self._request('POST', 'pgroup', data)