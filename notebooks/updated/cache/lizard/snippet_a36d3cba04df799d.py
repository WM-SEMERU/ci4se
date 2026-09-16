def create_or_update_group(self, name, policies=None, mount_point=
    DEFAULT_MOUNT_POINT):
    if policies is None:
        policies = []
    if not isinstance(policies, list):
        error_msg = (
            '"policies" argument must be an instance of list or None, "{policies_type}" provided.'
            .format(policies_type=type(policies)))
        raise exceptions.ParamValidationError(error_msg)
    params = {'policies': ','.join(policies)}
    api_path = '/v1/auth/{mount_point}/groups/{name}'.format(mount_point=
        mount_point, name=name)
    return self._adapter.post(url=api_path, json=params)