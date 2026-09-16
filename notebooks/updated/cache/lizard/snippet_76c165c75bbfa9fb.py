def diff(self):
    resp = self._get(self._api, headers={'Accept':
        'application/vnd.github.diff'})
    return resp.content if self._boolean(resp, 200, 404) else None