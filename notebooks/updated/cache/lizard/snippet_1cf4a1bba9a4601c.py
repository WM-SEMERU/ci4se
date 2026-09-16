def _set_namespace(self, namespaces):
    self.namespace = {}
    for m in namespaces[::-1]:
        buf = _get_namespace(m)
        self.namespace.update(buf)
    self.namespace.update(self.__dict__)