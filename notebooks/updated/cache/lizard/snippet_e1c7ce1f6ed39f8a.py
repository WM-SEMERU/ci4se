def get_port_map(self, id_or_uri):
    uri = self._client.build_uri(id_or_uri) + self.PORT_MAP_PATH
    return self._client.get(id_or_uri=uri)