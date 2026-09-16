def list_consumers_for_vhost(self, vhost):
    return self._api_get('/api/consumers/{0}'.format(urllib.parse.
        quote_plus(vhost)))