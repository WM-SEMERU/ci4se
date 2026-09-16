def find_by_name(self, name):
    uri = self._name_uri_cache.get(name)
    obj = self.resource_class(manager=self, uri=uri, name=name, properties=None
        )
    return obj