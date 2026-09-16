def get_content_unscoped_package(self, feed_id, package_name,
    package_version, **kwargs):
    route_values = {}
    if feed_id is not None:
        route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
    if package_name is not None:
        route_values['packageName'] = self._serialize.url('package_name',
            package_name, 'str')
    if package_version is not None:
        route_values['packageVersion'] = self._serialize.url('package_version',
            package_version, 'str')
    response = self._send(http_method='GET', location_id=
        '75caa482-cb1e-47cd-9f2c-c048a4b7a43e', version='5.0-preview.1',
        route_values=route_values, accept_media_type='application/octet-stream'
        )
    if 'callback' in kwargs:
        callback = kwargs['callback']
    else:
        callback = None
    return self._client.stream_download(response, callback=callback)