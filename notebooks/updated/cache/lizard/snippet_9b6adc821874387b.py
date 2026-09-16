def _send_message(self, method, endpoint, params=None, data=None):
    url = self.url + endpoint
    r = self.session.request(method, url, params=params, data=data, auth=
        self.auth, timeout=30)
    return r.json()