def get_tracks(self):
    return _extract_tracks(self._request(self.ws_prefix + '.getInfo',
        cacheable=True), self.network)