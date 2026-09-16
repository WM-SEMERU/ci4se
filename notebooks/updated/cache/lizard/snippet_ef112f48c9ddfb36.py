def update_build(self, build, project, build_id, retry=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if build_id is not None:
        route_values['buildId'] = self._serialize.url('build_id', build_id,
            'int')
    query_parameters = {}
    if retry is not None:
        query_parameters['retry'] = self._serialize.query('retry', retry,
            'bool')
    content = self._serialize.body(build, 'Build')
    response = self._send(http_method='PATCH', location_id=
        '0cd358e1-9217-4d94-8269-1c1ee6f93dcf', version='5.0', route_values
        =route_values, query_parameters=query_parameters, content=content)
    return self._deserialize('Build', response)