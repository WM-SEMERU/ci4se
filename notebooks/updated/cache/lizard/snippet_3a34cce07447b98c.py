def iter_network_events(self, number=-1, etag=None):
    base = self._api.replace('repos', 'networks', 1)
    url = self._build_url('events', base_url=base)
    return self._iter(int(number), url, Event, etag)