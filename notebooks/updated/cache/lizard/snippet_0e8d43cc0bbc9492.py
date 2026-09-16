def get_cherry_pick_for_ref_name(self, project, repository_id, ref_name):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if repository_id is not None:
        route_values['repositoryId'] = self._serialize.url('repository_id',
            repository_id, 'str')
    query_parameters = {}
    if ref_name is not None:
        query_parameters['refName'] = self._serialize.query('ref_name',
            ref_name, 'str')
    response = self._send(http_method='GET', location_id=
        '033bad68-9a14-43d1-90e0-59cb8856fef6', version='5.1-preview.1',
        route_values=route_values, query_parameters=query_parameters)
    return self._deserialize('GitCherryPick', response)