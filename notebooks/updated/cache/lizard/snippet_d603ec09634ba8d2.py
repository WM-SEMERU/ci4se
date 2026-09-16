def transit_generate_rand_bytes(self, data_bytes=None, output_format=None,
    mount_point='transit'):
    if data_bytes is not None:
        url = '/v1/{0}/random/{1}'.format(mount_point, data_bytes)
    else:
        url = '/v1/{0}/random'.format(mount_point)
    params = {}
    if output_format is not None:
        params['format'] = output_format
    return self._adapter.post(url, json=params).json()