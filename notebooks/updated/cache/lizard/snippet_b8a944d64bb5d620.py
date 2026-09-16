def remove_all(self, filter, force=False, timeout=-1):
    return self._client.delete_all(filter=filter, force=force, timeout=timeout)