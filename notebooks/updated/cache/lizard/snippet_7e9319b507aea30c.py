def hash(self, hash):
    self.md5 = None
    self.sha1 = None
    self.sha256 = None
    if hash is None:
        return
    hash_seen = set()
    errors = []
    for entry in hash.split():
        hash_type, value = entry.split(':', 1)
        if hash_type in hash_seen:
            errors.append('Ignored duplicate hash type %s' % hash_type)
        else:
            hash_seen.add(hash_type)
            if hash_type == 'md5':
                self.md5 = value
            elif hash_type == 'sha-1':
                self.sha1 = value
            elif hash_type == 'sha-256':
                self.sha256 = value
            else:
                errors.append('Ignored unsupported hash type (%s)' % hash_type)
    if len(errors) > 0:
        raise ValueError('. '.join(errors))