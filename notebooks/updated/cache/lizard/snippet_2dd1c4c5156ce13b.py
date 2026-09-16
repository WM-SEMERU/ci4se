def trim_key(self, name, min_version, mount_point=DEFAULT_MOUNT_POINT):
    params = {'min_available_version': min_version}
    api_path = '/v1/{mount_point}/keys/{name}/trim'.format(mount_point=
        mount_point, name=name)
    return self._adapter.post(url=api_path, json=params)