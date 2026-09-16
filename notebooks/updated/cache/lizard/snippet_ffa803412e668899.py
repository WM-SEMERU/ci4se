def transit_hash_data(self, hash_input, algorithm=None, output_format=None,
    mount_point='transit'):
    if algorithm is not None:
        url = '/v1/{0}/hash/{1}'.format(mount_point, algorithm)
    else:
        url = '/v1/{0}/hash'.format(mount_point)
    params = {'input': hash_input}
    if output_format is not None:
        params['format'] = output_format
    return self._adapter.post(url, json=params).json()