def list_versions(self):
    target_url = self._client.get_url('VERSION', 'GET', 'multi', {
        'layer_id': self.id})
    return base.Query(self._manager, target_url, valid_filter_attributes=(
        'data',), valid_sort_attributes=())