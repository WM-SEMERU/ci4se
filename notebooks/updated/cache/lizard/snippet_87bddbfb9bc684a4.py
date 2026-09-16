def create_or_update_secret(self, path, secret, method=None, mount_point=
    DEFAULT_MOUNT_POINT):
    if method is None:
        try:
            self.read_secret(path=path, mount_point=mount_point)
            method = 'PUT'
        except exceptions.InvalidPath:
            method = 'POST'
    if method == 'POST':
        api_path = '/v1/{mount_point}/{path}'.format(mount_point=
            mount_point, path=path)
        return self._adapter.post(url=api_path, json=secret)
    elif method == 'PUT':
        api_path = '/v1/{mount_point}/{path}'.format(mount_point=
            mount_point, path=path)
        return self._adapter.post(url=api_path, json=secret)
    else:
        error_message = (
            '"method" parameter provided invalid value; POST or PUT allowed, "{method}" provided'
            .format(method=method))
        raise exceptions.ParamValidationError(error_message)