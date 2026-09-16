def activate(self, key):
    url = self._base + 'user/activate'
    r = requests.get(url, params={'activation_key': key})
    r.raise_for_status()