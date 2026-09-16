def create_vhost(self, name, tracing=False):
    data = {'tracing': True} if tracing else {}
    self._api_put('/api/vhosts/{0}'.format(urllib.parse.quote_plus(name)),
        data=data)