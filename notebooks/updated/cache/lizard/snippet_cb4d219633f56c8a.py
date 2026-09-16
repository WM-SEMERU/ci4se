def register(self, uri, prefix):
    if not is_valid_schema_uri(uri):
        raise KeyError('cannot register invalid URI {} (prefix {})'.format(
            uri, prefix))
    if not is_valid_prefix(prefix):
        raise ValueError('cannot register invalid prefix %q for URI %q'.
            format(prefix, uri))
    if self._uri_to_prefix.get(uri) is None:
        self._uri_to_prefix[uri] = prefix