def transit_export_key(self, name, key_type, version=None, mount_point=
    'transit'):
    if version is not None:
        url = '/v1/{0}/export/{1}/{2}/{3}'.format(mount_point, key_type,
            name, version)
    else:
        url = '/v1/{0}/export/{1}/{2}'.format(mount_point, key_type, name)
    return self._adapter.get(url).json()