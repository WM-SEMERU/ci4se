def setArg(self, namespace, key, value):
    assert key is not None
    assert value is not None
    namespace = self._fixNS(namespace)
    if isinstance(value, bytes):
        value = str(value, encoding='utf-8')
    self.args[namespace, key] = value
    if not namespace is BARE_NS:
        self.namespaces.add(namespace)