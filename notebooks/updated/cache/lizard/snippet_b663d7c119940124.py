def get_event(self, client, check):
    data = self._request('GET', '/events/{}/{}'.format(client, check))
    return data.json()