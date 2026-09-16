def delete_build(self, project, build_id):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if build_id is not None:
        route_values['buildId'] = self._serialize.url('build_id', build_id,
            'int')
    self._send(http_method='DELETE', location_id=
        '0cd358e1-9217-4d94-8269-1c1ee6f93dcf', version='5.0', route_values
        =route_values)