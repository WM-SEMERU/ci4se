def parse(self, sentence, params=None, headers=None):
    if params is None:
        params = {}
    params['input'] = sentence
    hdrs = {'Accept': 'application/json'}
    if headers is not None:
        hdrs.update(headers)
    url = urljoin(self.server, 'parse')
    r = requests.get(url, params=params, headers=hdrs)
    if r.status_code == 200:
        return _RestResponse(r.json())
    else:
        r.raise_for_status()