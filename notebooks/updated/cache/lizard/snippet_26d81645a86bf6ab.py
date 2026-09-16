def get_changeset_work_items(self, id=None):
    route_values = {}
    if id is not None:
        route_values['id'] = self._serialize.url('id', id, 'int')
    response = self._send(http_method='GET', location_id=
        '64ae0bea-1d71-47c9-a9e5-fe73f5ea0ff4', version='5.0', route_values
        =route_values)
    return self._deserialize('[AssociatedWorkItem]', self.
        _unwrap_collection(response))