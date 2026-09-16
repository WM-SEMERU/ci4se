def _build_qname(self, uri=None, namespaces=None):
    if not uri:
        uri = self.uri
    if not namespaces:
        namespaces = self.namespaces
    return uri2niceString(uri, namespaces)