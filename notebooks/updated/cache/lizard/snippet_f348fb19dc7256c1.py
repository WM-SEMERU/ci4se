def _update_mappings(self):
    headers = {'Content-Type': 'application/json', 'DB-Method': 'PUT'}
    url = '/v2/exchange/db/{}/{}/_mappings'.format(self.domain, self.data_type)
    r = self.tcex.session.post(url, json=self.mapping, headers=headers)
    self.tcex.log.debug('update mapping. status_code: {}, response: "{}".'.
        format(r.status_code, r.text))