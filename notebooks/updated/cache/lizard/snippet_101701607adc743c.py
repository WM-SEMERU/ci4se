def query_data_providers(self, query, scope_name=None, scope_value=None):
    route_values = {}
    if scope_name is not None:
        route_values['scopeName'] = self._serialize.url('scope_name',
            scope_name, 'str')
    if scope_value is not None:
        route_values['scopeValue'] = self._serialize.url('scope_value',
            scope_value, 'str')
    content = self._serialize.body(query, 'DataProviderQuery')
    response = self._send(http_method='POST', location_id=
        '738368db-35ee-4b85-9f94-77ed34af2b0d', version='5.0-preview.1',
        route_values=route_values, content=content)
    return self._deserialize('DataProviderResult', response)