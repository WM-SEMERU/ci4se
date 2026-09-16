def get_hash(self, ireq, ireq_hashes=None):
    if not self._should_include_hash(ireq):
        return set()
    elif self._should_include_hash(ireq) and (not ireq_hashes or ireq.link.
        scheme == 'file'):
        if not ireq_hashes:
            ireq_hashes = set()
        new_hashes = self.resolver.repository._hash_cache.get_hash(ireq.link)
        ireq_hashes = add_to_set(ireq_hashes, new_hashes)
    else:
        ireq_hashes = set(ireq_hashes)
    if ireq not in self.hashes:
        return ireq_hashes
    else:
        return self.hashes[ireq] | ireq_hashes