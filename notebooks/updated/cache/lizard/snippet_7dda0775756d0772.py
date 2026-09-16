def save(self, with_data=False):
    target_url = self._client.get_url('VERSION', 'PUT', 'edit', {'layer_id':
        self.id, 'version_id': self.version.id})
    r = self._client.request('PUT', target_url, json=self._serialize(
        with_data=with_data))
    return self._deserialize(r.json(), self._manager)