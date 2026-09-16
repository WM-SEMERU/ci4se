def get_endpoint_by_endpoint_id(self, endpoint_id):
    self._validate_uuid(endpoint_id)
    url = '/notification/v1/endpoint/{}'.format(endpoint_id)
    response = NWS_DAO().getURL(url, self._read_headers)
    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)
    data = json.loads(response.data)
    return self._endpoint_from_json(data.get('Endpoint'))