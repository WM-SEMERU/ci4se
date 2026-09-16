def update(self, body):
    json = None
    if body:
        json = self._json(self._post(self._api, data={'body': body}), 200)
    if json:
        self._update_(json)
        return True
    return False