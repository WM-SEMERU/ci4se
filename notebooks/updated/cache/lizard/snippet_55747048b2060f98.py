def publish(self, version_id=None):
    if not version_id:
        version_id = self.version.id
    target_url = self._client.get_url('VERSION', 'POST', 'publish', {
        'layer_id': self.id, 'version_id': version_id})
    r = self._client.request('POST', target_url, json={})
    return self._client.get_manager(Publish).create_from_result(r.json())