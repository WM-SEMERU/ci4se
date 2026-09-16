def token(self):
    if self._token is None or datetime.datetime.now(
        ) >= self._token_expires_on:
        if self._referer_url is None:
            result = self._generateForTokenSecurity(username=self._username,
                password=self._password, tokenUrl=self._token_url)
        else:
            result = self._generateForTokenSecurity(username=self._username,
                password=self._password, tokenUrl=self._token_url, client=
                'referer')
        if 'error' in result:
            self._valid = False
            self._message = result
        else:
            self._valid = True
            self._message = 'Token Generated'
    return self._token