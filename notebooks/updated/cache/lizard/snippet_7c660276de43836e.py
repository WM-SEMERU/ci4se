def request(self, scheme, url, data=None, params=None):
    url = self.url.format(self.team, url)
    headers = {'X-MiteApikey': self.api_key, 'User-Agent':
        'mite Python wrapper: https://github.com/port-zero/mite',
        'Content-Type': 'application/json'}
    fn = requests.__getattribute__(scheme)
    res = fn(url, headers=headers, json=data, params=params)
    if res.status_code >= 300:
        self._raise_exception(res.status_code)
    if not res.content:
        return None
    try:
        return res.json()
    except ValueError:
        return res.content