def rename(self, old, new):
    old_key = _make_key(old)
    new_key = _make_key(new)
    logger.debug('Renaming relation {!s} to {!s}'.format(old_key, new_key))
    logger.debug('before rename: {}'.format(pprint.pformat(self.dump_graph())))
    with self.lock:
        if self._check_rename_constraints(old_key, new_key):
            self._rename_relation(old_key, _CachedRelation(new))
        else:
            self._setdefault(_CachedRelation(new))
    logger.debug('after rename: {}'.format(pprint.pformat(self.dump_graph())))