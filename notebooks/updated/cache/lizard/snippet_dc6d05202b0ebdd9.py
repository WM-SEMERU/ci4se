def get_endpoint_by_subscriber_id_and_protocol(self, subscriber_id, protocol):
    self._validate_subscriber_id(subscriber_id)
    self._validate_endpoint_protocol(protocol)
    url = '/notification/v1/endpoint?subscriber_id={}&protocol={}'.format(
        subscriber_id, protocol)
    response = NWS_DAO().getURL(url, self._read_headers)
    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)
    data = json.loads(response.data)
    try:
        return self._endpoint_from_json(data.get('Endpoints')[0])
    except IndexError:
        raise DataFailureException(url, 404, 'No SMS endpoint found')