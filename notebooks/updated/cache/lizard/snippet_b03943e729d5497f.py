def search_datasets(self, license=None, format=None, query=None, featured=
    None, owner=None, organization=None, badge=None, reuses=None, page_size
    =20, x_fields=None):
    payload = {'badge': badge, 'size': page_size, 'X-Fields': x_fields}
    search_url = '{}/datasets'.format(self.base_url)
    search_req = requests.get(search_url, params=payload)
    logger.debug(search_req.url)
    return search_req.json()