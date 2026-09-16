def _hash(self, hash_name):
    m = hashlib.new(hash_name)
    for chunk in self.chunks(8192, mode='rb'):
        m.update(chunk)
    return m