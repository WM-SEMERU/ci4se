def increment_extension_daily_stat(self, publisher_name, extension_name,
    version, stat_type):
    route_values = {}
    if publisher_name is not None:
        route_values['publisherName'] = self._serialize.url('publisher_name',
            publisher_name, 'str')
    if extension_name is not None:
        route_values['extensionName'] = self._serialize.url('extension_name',
            extension_name, 'str')
    if version is not None:
        route_values['version'] = self._serialize.url('version', version, 'str'
            )
    query_parameters = {}
    if stat_type is not None:
        query_parameters['statType'] = self._serialize.query('stat_type',
            stat_type, 'str')
    self._send(http_method='POST', location_id=
        '4fa7adb6-ca65-4075-a232-5f28323288ea', version='5.0-preview.1',
        route_values=route_values, query_parameters=query_parameters)