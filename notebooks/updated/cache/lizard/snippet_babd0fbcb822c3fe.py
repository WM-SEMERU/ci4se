def get_web_auth_url(self):
    token = self._get_web_auth_token()
    url = '{homepage}/api/auth/?api_key={api}&token={token}'.format(homepage
        =self.network.homepage, api=self.network.api_key, token=token)
    self.web_auth_tokens[url] = token
    return url