def _create_and_update(self):
    data_json = self._create_json()
    data_json.update(self.additional_params)
    request_url = self._artifactory.drive + '/api/{uri}/{x.name}'.format(uri
        =self._uri, x=self)
    r = self._session.put(request_url, json=data_json, headers={
        'Content-Type': 'application/json'}, auth=self._auth)
    r.raise_for_status()
    rest_delay()
    self.read()