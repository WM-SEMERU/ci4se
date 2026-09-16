def list(self, includes=None, doc_type=None, promulgated_only=False, sort=
    None, owner=None, series=None):
    queries = self._common_query_parameters(doc_type, includes, owner,
        promulgated_only, series, sort)
    if len(queries):
        url = '{}/list?{}'.format(self.url, urlencode(queries))
    else:
        url = '{}/list'.format(self.url)
    data = self._get(url)
    return data.json()['Results']