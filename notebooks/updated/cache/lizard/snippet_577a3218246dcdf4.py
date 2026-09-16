def get_package_version(self, feed_id, package_name, package_version,
    show_deleted=None):
    route_values = {}
    if feed_id is not None:
        route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
    if package_name is not None:
        route_values['packageName'] = self._serialize.url('package_name',
            package_name, 'str')
    if package_version is not None:
        route_values['packageVersion'] = self._serialize.url('package_version',
            package_version, 'str')
    query_parameters = {}
    if show_deleted is not None:
        query_parameters['showDeleted'] = self._serialize.query('show_deleted',
            show_deleted, 'bool')
    response = self._send(http_method='GET', location_id=
        'd146ac7e-9e3f-4448-b956-f9bb3bdf9b2e', version='5.0-preview.1',
        route_values=route_values, query_parameters=query_parameters)
    return self._deserialize('Package', response)