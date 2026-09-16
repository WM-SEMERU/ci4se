def get(self, external_site: str, external_id: int):
    r = requests.get(self.apiurl + '/mappings', params={
        'filter[externalSite]': external_site, 'filter[externalId]':
        external_id}, headers=self.header)
    if r.status_code != 200:
        raise ServerError
    jsd = r.json()
    if len(jsd['data']) < 1:
        return None
    r = requests.get(jsd['data'][0]['relationships']['item']['links'][
        'related'], headers=self.header)
    if r.status_code != 200:
        return jsd
    else:
        return r.json()