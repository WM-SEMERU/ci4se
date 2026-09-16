def execute(self, interactive=False):
    url = self._client._build_url('service_execute', service_id=self.id)
    response = self._client._request('GET', url, params=dict(interactive=
        interactive, format='json'))
    if response.status_code != requests.codes.accepted:
        raise APIError("Could not execute service '{}': {}".format(self, (
            response.status_code, response.json())))
    data = response.json()
    return ServiceExecution(json=data.get('results')[0], client=self._client)