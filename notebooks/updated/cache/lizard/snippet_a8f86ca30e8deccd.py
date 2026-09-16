def login(self, token, use_token=True, mount_point=DEFAULT_MOUNT_POINT):
    params = {'token': token}
    api_path = '/v1/auth/{mount_point}/login'.format(mount_point=mount_point)
    return self._adapter.login(url=api_path, use_token=use_token, json=params)