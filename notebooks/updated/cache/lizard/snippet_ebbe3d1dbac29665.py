def get_by_resource(self, resource_uri):
    uri = self.URI + self.RESOURCES_PATH + '/' + resource_uri
    return self._client.get(id_or_uri=uri)