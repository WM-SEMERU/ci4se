def update(self, resource, id_or_uri=None, timeout=-1):
    uri = resource.pop('uri', None)
    if not uri:
        if not id_or_uri:
            raise ValueError('URI was not provided')
        uri = self._client.build_uri(id_or_uri)
    return self._client.update(resource=resource, uri=uri, timeout=timeout)