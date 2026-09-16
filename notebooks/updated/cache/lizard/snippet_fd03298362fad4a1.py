def read_secret_version(self, path, version=None, mount_point=
    DEFAULT_MOUNT_POINT):
    params = {}
    if version is not None:
        params['version'] = version
    api_path = '/v1/{mount_point}/data/{path}'.format(mount_point=
        mount_point, path=path)
    response = self._adapter.get(url=api_path, params=params)
    return response.json()