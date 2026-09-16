def create_resources(self, creation_parameters, project):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    content = self._serialize.body(creation_parameters,
        '{ResourceCreationParameter}')
    response = self._send(http_method='POST', location_id=
        '43201899-7690-4870-9c79-ab69605f21ed', version='5.1-preview.1',
        route_values=route_values, content=content)
    return self._deserialize('CreatedResources', response)