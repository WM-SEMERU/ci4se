def insert_or_merge_entity(self, table_name, entity, timeout=None):
    _validate_not_none('table_name', table_name)
    request = _insert_or_merge_entity(entity)
    request.host = self._get_host()
    request.query += [('timeout', _int_to_str(timeout))]
    request.path = _get_entity_path(table_name, entity['PartitionKey'],
        entity['RowKey'])
    response = self._perform_request(request)
    return _extract_etag(response)