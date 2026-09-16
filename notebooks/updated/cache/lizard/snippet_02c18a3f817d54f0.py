def create_folder(self, folder, project, path):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if path is not None:
        route_values['path'] = self._serialize.url('path', path, 'str')
    content = self._serialize.body(folder, 'Folder')
    response = self._send(http_method='PUT', location_id=
        'a906531b-d2da-4f55-bda7-f3e676cc50d9', version='5.0-preview.2',
        route_values=route_values, content=content)
    return self._deserialize('Folder', response)