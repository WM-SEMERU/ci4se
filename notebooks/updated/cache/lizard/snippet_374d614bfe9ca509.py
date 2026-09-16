def get_fields(self, project=None, expand=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    query_parameters = {}
    if expand is not None:
        query_parameters['$expand'] = self._serialize.query('expand',
            expand, 'str')
    response = self._send(http_method='GET', location_id=
        'b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94', version='5.0', route_values
        =route_values, query_parameters=query_parameters)
    return self._deserialize('[WorkItemField]', self._unwrap_collection(
        response))