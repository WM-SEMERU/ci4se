def get_osdp(self, id_or_uri):
    uri = self._client.build_subresource_uri(resource_id_or_uri=id_or_uri,
        subresource_path='osdp')
    return self._client.get(uri)