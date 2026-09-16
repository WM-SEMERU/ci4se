def get_ports(self, id_or_uri, start=0, count=-1):
    uri = self._client.build_subresource_uri(resource_id_or_uri=id_or_uri,
        subresource_path='ports')
    return self._client.get_all(start, count, uri=uri)