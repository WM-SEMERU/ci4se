def get_list(self, size=100, startIndex=0, searchText='', sortProperty='',
    sortOrder='ASC', status='Active,Pending'):
    url = urljoin(BASEURL, 'sites', 'list')
    params = {'api_key': self.token, 'size': size, 'startIndex': startIndex,
        'sortOrder': sortOrder, 'status': status}
    if searchText:
        params['searchText'] = searchText
    if sortProperty:
        params['sortProperty'] = sortProperty
    r = requests.get(url, params)
    r.raise_for_status()
    return r.json()