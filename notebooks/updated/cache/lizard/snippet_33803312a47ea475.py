def _post(self, q, payload='', params=''):
    if q[-1] == '/':
        q = q[:-1]
    headers = {'Content-Type': 'application/json'}
    r = requests.post('{url}{q}?api_key={key}{params}'.format(url=self.url,
        q=q, key=self.api_key, params=params), headers=headers, data=payload)
    ret = DotDict(r.json())
    if not r.ok or 'error' in ret and ret.error == True:
        raise Exception(r.url, r.reason, r.status_code, r.json())
    return DotDict(r.json())