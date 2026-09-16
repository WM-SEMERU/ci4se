def index_exists(self):
    headers = {'Content-Type': 'application/json', 'DB-Method': 'GET'}
    url = '/v2/exchange/db/{}/{}/_search'.format(self.domain, self.data_type)
    r = self.tcex.session.post(url, headers=headers)
    if not r.ok:
        self.tcex.log.warning('The provided index was not found ({}).'.
            format(r.text))
        return False
    return True