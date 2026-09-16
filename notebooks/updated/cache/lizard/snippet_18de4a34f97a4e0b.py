def get_revision(self, id, revision_number, project=None, expand=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if id is not None:
        route_values['id'] = self._serialize.url('id', id, 'int')
    if revision_number is not None:
        route_values['revisionNumber'] = self._serialize.url('revision_number',
            revision_number, 'int')
    query_parameters = {}
    if expand is not None:
        query_parameters['$expand'] = self._serialize.query('expand',
            expand, 'str')
    response = self._send(http_method='GET', location_id=
        'a00c85a5-80fa-4565-99c3-bcd2181434bb', version='5.1-preview.3',
        route_values=route_values, query_parameters=query_parameters)
    return self._deserialize('WorkItem', response)