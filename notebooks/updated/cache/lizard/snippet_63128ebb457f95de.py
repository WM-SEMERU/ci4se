def startPrefixMapping(self, prefix, uri, *, auto=False):
    if prefix is not None and (prefix == 'xml' or prefix == 'xmlns' or not
        xmlValidateNameValue_str(prefix) or ':' in prefix):
        raise ValueError('not a valid prefix: {!r}'.format(prefix))
    if prefix in self._ns_prefixes_floating_in:
        raise ValueError('prefix already declared for next element')
    if auto:
        self._ns_auto_prefixes_floating_in.add(prefix)
    self._ns_prefixes_floating_in[prefix] = uri
    self._ns_decls_floating_in[uri] = prefix