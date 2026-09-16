def verify(self, checksum=None, token=None, full_response=False):
    payload = {'checksum': checksum, 'a': 'verify'}
    if token:
        payload.update({'token': token})
    return self.get_shards(Shard(**payload), full_response=True)