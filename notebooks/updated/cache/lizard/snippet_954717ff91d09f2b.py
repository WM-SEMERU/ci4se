def _fingerprint_target_specs(self, specs):
    assert self._build_graph is not None, 'cannot fingerprint specs `{}` without a `BuildGraph`'.format(
        specs)
    hasher = sha1()
    for spec in sorted(specs):
        for target in sorted(self._build_graph.resolve(spec)):
            h = target.compute_invalidation_hash()
            if h:
                hasher.update(h.encode('utf-8'))
    return hasher.hexdigest()