def get_label_items(self, label_id, top=None, skip=None):
    route_values = {}
    if label_id is not None:
        route_values['labelId'] = self._serialize.url('label_id', label_id,
            'str')
    query_parameters = {}
    if top is not None:
        query_parameters['$top'] = self._serialize.query('top', top, 'int')
    if skip is not None:
        query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
    response = self._send(http_method='GET', location_id=
        '06166e34-de17-4b60-8cd1-23182a346fda', version='5.0', route_values
        =route_values, query_parameters=query_parameters)
    return self._deserialize('[TfvcItem]', self._unwrap_collection(response))