def get_build_logs_zip(self, project, build_id, **kwargs):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if build_id is not None:
        route_values['buildId'] = self._serialize.url('build_id', build_id,
            'int')
    response = self._send(http_method='GET', location_id=
        '35a80daf-7f30-45fc-86e8-6b813d9c90df', version='5.0', route_values
        =route_values, accept_media_type='application/zip')
    if 'callback' in kwargs:
        callback = kwargs['callback']
    else:
        callback = None
    return self._client.stream_download(response, callback=callback)