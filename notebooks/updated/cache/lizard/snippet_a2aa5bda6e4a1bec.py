def query_entities(self, table_name, filter=None, select=None, num_results=
    None, marker=None, accept=TablePayloadFormat.JSON_MINIMAL_METADATA,
    property_resolver=None, timeout=None):
    operation_context = _OperationContext(location_lock=True)
    if (self.key_encryption_key is not None or self.key_resolver_function
         is not None):
        if select is not None and select != '*':
            select += ',_ClientEncryptionMetadata1,_ClientEncryptionMetadata2'
    args = table_name,
    kwargs = {'filter': filter, 'select': select, 'max_results':
        num_results, 'marker': marker, 'accept': accept,
        'property_resolver': property_resolver, 'timeout': timeout,
        '_context': operation_context}
    resp = self._query_entities(*args, **kwargs)
    return ListGenerator(resp, self._query_entities, args, kwargs)