def sync(self, old_token=None):
    token = 'http://radicale.org/ns/sync/%s' % self.etag.strip('"')
    if old_token:
        raise ValueError(
            'Sync token are not supported (you can ignore this warning)')
    return token, self.list()