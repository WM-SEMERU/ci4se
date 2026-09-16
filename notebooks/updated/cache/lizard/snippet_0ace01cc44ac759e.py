def decode(self, key):
    key = BucketKey.decode(key)
    if key.uuid != self.uuid:
        raise ValueError('%s is not a bucket corresponding to this limit' % key
            )
    return key.params