def delete_policy_configuration(self, project, configuration_id):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if configuration_id is not None:
        route_values['configurationId'] = self._serialize.url(
            'configuration_id', configuration_id, 'int')
    self._send(http_method='DELETE', location_id=
        'dad91cbe-d183-45f8-9c6e-9c1164472121', version='5.0', route_values
        =route_values)