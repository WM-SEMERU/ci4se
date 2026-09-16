def query(self, api_token, queries, **kwargs):
    params = {'token': api_token, 'queries': queries}
    return self._get('query', params, **kwargs)