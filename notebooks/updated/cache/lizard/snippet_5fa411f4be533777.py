def remove_synchronous(self, resource, force=False, timeout=-1):
    uri = self._client.build_uri(resource['uri']) + '/synchronous'
    remove_resource = {'uri': uri}
    return self._client.delete(remove_resource, force=force, timeout=timeout)