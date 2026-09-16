def create(self, key, value):
    key = quote(key, safe='~')
    headers = {'content-type': 'application/octet-stream'}
    url = '/internal/playbooks/keyValue/{}'.format(key)
    r = self.tcex.session.put(url, data=value, headers=headers)
    return r.content