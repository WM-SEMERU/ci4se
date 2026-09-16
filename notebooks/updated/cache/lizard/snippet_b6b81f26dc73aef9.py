def iter_events(self, public=False, number=-1, etag=None):
    path = ['events']
    if public:
        path.append('public')
    url = self._build_url(*path, base_url=self._api)
    return self._iter(int(number), url, Event, etag=etag)