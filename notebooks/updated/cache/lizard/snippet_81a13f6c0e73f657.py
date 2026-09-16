def get_entity(self, table_name, partition_key, row_key, select=None,
    accept=TablePayloadFormat.JSON_MINIMAL_METADATA, property_resolver=None,
    timeout=None):
    _validate_not_none('table_name', table_name)
    request = _get_entity(partition_key, row_key, select, accept)
    request.host = self._get_host()
    request.path = _get_entity_path(table_name, partition_key, row_key)
    request.query += [('timeout', _int_to_str(timeout))]
    response = self._perform_request(request)
    return _convert_json_response_to_entity(response, property_resolver)