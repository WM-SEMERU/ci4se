def __CheckAndUnifyQueryFormat(self, query_body):
    if (self._query_compatibility_mode == CosmosClient.
        _QueryCompatibilityMode.Default or self._query_compatibility_mode ==
        CosmosClient._QueryCompatibilityMode.Query):
        if not isinstance(query_body, dict) and not isinstance(query_body,
            six.string_types):
            raise TypeError('query body must be a dict or string.')
        if isinstance(query_body, dict) and not query_body.get('query'):
            raise ValueError(
                'query body must have valid query text with key "query".')
        if isinstance(query_body, six.string_types):
            return {'query': query_body}
    elif self._query_compatibility_mode == CosmosClient._QueryCompatibilityMode.SqlQuery and not isinstance(
        query_body, six.string_types):
        raise TypeError('query body must be a string.')
    else:
        raise SystemError('Unexpected query compatibility mode.')
    return query_body