def setOpenIDNamespace(self, openid_ns_uri, implicit):
    if isinstance(openid_ns_uri, bytes):
        openid_ns_uri = str(openid_ns_uri, encoding='utf-8')
    if openid_ns_uri not in self.allowed_openid_namespaces:
        raise InvalidOpenIDNamespace(openid_ns_uri)
    self.namespaces.addAlias(openid_ns_uri, NULL_NAMESPACE, implicit)
    self._openid_ns_uri = openid_ns_uri