def start_import(self, version_id=None):
    if not version_id:
        version_id = self.version.id
    target_url = self._client.get_url('VERSION', 'POST', 'import', {
        'layer_id': self.id, 'version_id': version_id})
    r = self._client.request('POST', target_url, json={})
    return self._deserialize(r.json(), self._manager)