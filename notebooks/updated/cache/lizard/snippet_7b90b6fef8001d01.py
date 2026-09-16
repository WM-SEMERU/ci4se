def access_token(self):
    if self._access_token is None or self.expiration_time <= int(time.time()):
        resp = self.make_access_request()
        self._access_token = resp.json()['access_token']
    return self._access_token