def set_global_permissions(self, global_permissions):
    content = self._serialize.body(global_permissions, '[GlobalPermission]')
    response = self._send(http_method='PATCH', location_id=
        'a74419ef-b477-43df-8758-3cd1cd5f56c6', version='5.0-preview.1',
        content=content)
    return self._deserialize('[GlobalPermission]', self._unwrap_collection(
        response))