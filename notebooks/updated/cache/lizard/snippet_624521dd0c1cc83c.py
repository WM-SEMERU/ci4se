def get_items_batch_zip(self, item_request_data, project=None, **kwargs):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    content = self._serialize.body(item_request_data, 'TfvcItemRequestData')
    response = self._send(http_method='POST', location_id=
        'fe6f827b-5f64-480f-b8af-1eca3b80e833', version='5.0', route_values
        =route_values, content=content, accept_media_type='application/zip')
    if 'callback' in kwargs:
        callback = kwargs['callback']
    else:
        callback = None
    return self._client.stream_download(response, callback=callback)