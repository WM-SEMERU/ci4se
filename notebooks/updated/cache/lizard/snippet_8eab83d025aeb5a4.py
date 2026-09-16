def list_roles(self, mount_point=DEFAULT_MOUNT_POINT):
    api_path = '/v1/auth/{mount_point}/roles'.format(mount_point=mount_point)
    response = self._adapter.list(url=api_path)
    return response.json().get('data')