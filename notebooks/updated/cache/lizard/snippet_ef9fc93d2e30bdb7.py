def create_upload_url(self, upload_id, number, size, hash_value, hash_alg):
    if number < 1:
        raise ValueError('Chunk number must be > 0')
    data = {'number': number, 'size': size, 'hash': {'value': hash_value,
        'algorithm': hash_alg}}
    return self._put('/uploads/' + upload_id + '/chunks', data)