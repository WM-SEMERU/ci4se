def resize(self, new_size):
    self._client.post('{}/resize'.format(Disk.api_endpoint), model=self,
        data={'size': new_size})
    return True