def configure_lease(self, lease, lease_max, mount_point=DEFAULT_MOUNT_POINT):
    params = {'lease': lease, 'lease_max': lease_max}
    api_path = '/v1/{mount_point}/config/lease'.format(mount_point=mount_point)
    return self._adapter.post(url=api_path, json=params)