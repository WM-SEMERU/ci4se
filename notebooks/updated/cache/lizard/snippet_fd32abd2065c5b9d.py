def http_method(self, data):
    data = data.upper()
    if data in ['DELETE', 'GET', 'POST', 'PUT']:
        self._request.http_method = data
        self._http_method = data