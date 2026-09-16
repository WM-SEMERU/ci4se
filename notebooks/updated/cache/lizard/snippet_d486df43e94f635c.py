def _head(self, client_kwargs):
    return _handle_http_errors(self.client.request('HEAD', timeout=self.
        _TIMEOUT, **client_kwargs)).headers