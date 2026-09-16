def SetLookupHash(self, lookup_hash):
    if lookup_hash not in self.SUPPORTED_HASHES:
        raise ValueError('Unsupported lookup hash: {0!s}'.format(lookup_hash))
    self.lookup_hash = lookup_hash