def list(self, **kwds):
    tags = self._client.get('/tags/list.json', **kwds)['result']
    tags = self._result_to_list(tags)
    return [Tag(self._client, tag) for tag in tags]