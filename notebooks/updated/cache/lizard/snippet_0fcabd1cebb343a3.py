def read_user(self, username, mount_point=DEFAULT_MOUNT_POINT):
    params = {'username': username}
    api_path = '/v1/auth/{mount_point}/users/{username}'.format(mount_point
        =mount_point, username=username)
    response = self._adapter.get(url=api_path, json=params)
    return response.json()