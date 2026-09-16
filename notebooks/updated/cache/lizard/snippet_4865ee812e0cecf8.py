def logout(self):
    resp = super(CookieSession, self).request('DELETE', self._session_url)
    resp.raise_for_status()