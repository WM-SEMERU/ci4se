def http(self):
    if self._use_cached_http and hasattr(self._local, 'http'):
        return self._local.http
    if self._http_replay is not None:
        http = self._http_replay
    else:
        http = _build_http()
    authorized_http = google_auth_httplib2.AuthorizedHttp(self._credentials,
        http=http)
    if self._use_cached_http:
        self._local.http = authorized_http
    return authorized_http