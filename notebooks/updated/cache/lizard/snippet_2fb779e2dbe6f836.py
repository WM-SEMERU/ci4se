def transit_update_key(self, name, min_decryption_version=None,
    min_encryption_version=None, deletion_allowed=None, mount_point='transit'):
    url = '/v1/{0}/keys/{1}/config'.format(mount_point, name)
    params = {}
    if min_decryption_version is not None:
        params['min_decryption_version'] = min_decryption_version
    if min_encryption_version is not None:
        params['min_encryption_version'] = min_encryption_version
    if deletion_allowed is not None:
        params['deletion_allowed'] = deletion_allowed
    return self._adapter.post(url, json=params)