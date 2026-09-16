def setup_oauth_client(self, url=None):
    if url and '://' in url:
        server, endpoint = self._deconstruct_url(url)
    else:
        server = self.client.server
    if server not in self._server_cache:
        self._add_client(server)
    if server == self.client.server:
        self.oauth = OAuth1(client_key=self.store['client-key'],
            client_secret=self.store['client-secret'], resource_owner_key=
            self.store['oauth-access-token'], resource_owner_secret=self.
            store['oauth-access-secret'])
        return self.oauth
    else:
        return OAuth1(client_key=self._server_cache[server].key,
            client_secret=self._server_cache[server].secret)