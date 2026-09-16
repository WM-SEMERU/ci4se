def put(self, key, value, lease=None):
    payload = {'key': _encode(key), 'value': _encode(value)}
    if lease:
        payload['lease'] = lease.id
    self.post(self.get_url('/kv/put'), json=payload)
    return True