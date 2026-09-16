def servertoken(self, serverURL, referer):
    if (self._server_token is None or self._server_token_expires_on is None or
        datetime.datetime.now() >= self._server_token_expires_on or self.
        _server_url != serverURL):
        self._server_url = serverURL
        result = self._generateForServerTokenSecurity(serverURL=serverURL,
            token=self.token, tokenUrl=self._token_url, referer=referer)
        if 'error' in result:
            self._valid = False
            self._message = result
        else:
            self._valid = True
            self._message = 'Server Token Generated'
    return self._server_token