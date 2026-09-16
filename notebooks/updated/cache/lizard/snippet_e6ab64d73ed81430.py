def get_page(self, url):
    if url:
        data = self.feed._request(url, offset=self._offset, since=self.
            _since, before=self._before)
        self._before = False if self._before is not None else None
        self._since = False if self._since is not None else None
        if getattr(self.feed, 'issue65', False):
            self._offset = False
        if self._since is not None:
            return reversed(data['items'])
        else:
            return data['items']
    else:
        return []