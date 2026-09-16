def do_get(self, uri):
    self.validate_resource_uri(uri)
    return self._connection.get(uri)