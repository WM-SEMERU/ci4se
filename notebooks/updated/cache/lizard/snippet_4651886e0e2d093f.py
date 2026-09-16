def create(self, port, value, timestamp=None):
    session = self._session
    datapoint_class = self._datapoint_class
    attributes = {'port': port, 'value': value}
    if timestamp is not None:
        attributes['timestamp'] = to_iso_date(timestamp)
    attributes = build_request_body('data-point', None, attributes=attributes)

    def _process(json):
        data = json.get('data')
        return datapoint_class(data, session)
    return session.post(self._base_url, CB.json(201, _process), json=attributes
        )