def get_users_summary(self, select=None):
    query_parameters = {}
    if select is not None:
        query_parameters['select'] = self._serialize.query('select', select,
            'str')
    response = self._send(http_method='GET', location_id=
        '5ae55b13-c9dd-49d1-957e-6e76c152e3d9', version='5.0-preview.1',
        query_parameters=query_parameters)
    return self._deserialize('UsersSummary', response)