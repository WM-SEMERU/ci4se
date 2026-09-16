def isLoggedIn(self):
    r = self._cleanGet(self.req_url.LOGIN, allow_redirects=False)
    return 'Location' in r.headers and 'home' in r.headers['Location']