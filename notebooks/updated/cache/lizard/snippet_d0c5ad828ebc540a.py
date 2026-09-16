def create_or_update_role(self, name, credential_type, policy_document=None,
    default_sts_ttl=None, max_sts_ttl=None, role_arns=None, policy_arns=
    None, legacy_params=False, mount_point=DEFAULT_MOUNT_POINT):
    if credential_type not in ALLOWED_CREDS_TYPES:
        error_msg = (
            'invalid credential_type argument provided "{arg}", supported types: "{allowed_types}"'
            )
        raise exceptions.ParamValidationError(error_msg.format(arg=
            credential_type, allowed_types=', '.join(ALLOWED_CREDS_TYPES)))
    if isinstance(policy_document, dict):
        policy_document = json.dumps(policy_document, indent=4, sort_keys=True)
    if legacy_params:
        params = {'policy': policy_document, 'arn': policy_arns[0] if
            isinstance(policy_arns, list) else policy_arns}
    else:
        params = {'credential_type': credential_type, 'policy_document':
            policy_document, 'default_sts_ttl': default_sts_ttl,
            'max_sts_ttl': max_sts_ttl, 'role_arns': role_arns,
            'policy_arns': policy_arns}
    api_path = '/v1/{mount_point}/roles/{name}'.format(mount_point=
        mount_point, name=name)
    return self._adapter.post(url=api_path, json=params)