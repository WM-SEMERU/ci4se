def create_role(self, name, policies=None, ttl=None, max_ttl=None, period=
    None, bound_service_principal_ids=None, bound_group_ids=None,
    bound_location=None, bound_subscription_ids=None,
    bound_resource_group_names=None, bound_scale_sets=None, mount_point=
    DEFAULT_MOUNT_POINT):
    if policies is None:
        policies = []
    if not isinstance(policies, list) or not all([isinstance(p, str) for p in
        policies]):
        error_msg = (
            'unsupported policies argument provided "{arg}" ({arg_type}), required type: List[str]"'
            )
        raise exceptions.ParamValidationError(error_msg.format(arg=policies,
            arg_type=type(policies)))
    params = {'policies': policies, 'ttl': ttl, 'max_ttl': max_ttl,
        'period': period, 'bound_service_principal_ids':
        bound_service_principal_ids, 'bound_group_ids': bound_group_ids,
        'bound_location': bound_location, 'bound_subscription_ids':
        bound_subscription_ids, 'bound_resource_group_names':
        bound_resource_group_names, 'bound_scale_sets': bound_scale_sets}
    api_path = '/v1/auth/{mount_point}/role/{name}'.format(mount_point=
        mount_point, name=name)
    return self._adapter.post(url=api_path, json=params)