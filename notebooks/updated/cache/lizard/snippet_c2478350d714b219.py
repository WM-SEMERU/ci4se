def create_attachment(self, upload_stream, project=None, file_name=None,
    upload_type=None, area_path=None, **kwargs):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    query_parameters = {}
    if file_name is not None:
        query_parameters['fileName'] = self._serialize.query('file_name',
            file_name, 'str')
    if upload_type is not None:
        query_parameters['uploadType'] = self._serialize.query('upload_type',
            upload_type, 'str')
    if area_path is not None:
        query_parameters['areaPath'] = self._serialize.query('area_path',
            area_path, 'str')
    if 'callback' in kwargs:
        callback = kwargs['callback']
    else:
        callback = None
    content = self._client.stream_upload(upload_stream, callback=callback)
    response = self._send(http_method='POST', location_id=
        'e07b5fa4-1499-494d-a496-64b860fd64ff', version='5.0', route_values
        =route_values, query_parameters=query_parameters, content=content,
        media_type='application/octet-stream')
    return self._deserialize('AttachmentReference', response)