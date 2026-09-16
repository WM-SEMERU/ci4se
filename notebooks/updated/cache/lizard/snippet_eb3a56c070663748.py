def add(self, resource, provider_uri_or_id, timeout=-1):
    uri = self._provider_client.build_uri(provider_uri_or_id
        ) + '/device-managers'
    return self._client.create(resource=resource, uri=uri, timeout=timeout)