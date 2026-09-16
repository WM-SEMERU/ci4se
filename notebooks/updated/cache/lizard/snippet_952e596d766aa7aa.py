def transit_generate_hmac(self, name, hmac_input, key_version=None,
    algorithm=None, mount_point='transit'):
    if algorithm is not None:
        url = '/v1/{0}/hmac/{1}/{2}'.format(mount_point, name, algorithm)
    else:
        url = '/v1/{0}/hmac/{1}'.format(mount_point, name)
    params = {'input': hmac_input}
    if key_version is not None:
        params['key_version'] = key_version
    return self._adapter.post(url, json=params).json()