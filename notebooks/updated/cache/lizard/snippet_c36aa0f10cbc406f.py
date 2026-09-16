def update_build_settings(self, settings, project=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    content = self._serialize.body(settings, 'BuildSettings')
    response = self._send(http_method='PATCH', location_id=
        'aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d', version='5.0', route_values
        =route_values, content=content)
    return self._deserialize('BuildSettings', response)