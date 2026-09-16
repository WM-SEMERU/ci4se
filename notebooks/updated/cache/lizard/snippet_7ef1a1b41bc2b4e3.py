def unload(self, key):
    assert isinstance(key, PGPKey)
    pkid = id(key)
    if pkid in self._keys:
        [kd.remove(pkid) for kd in [self._pubkeys, self._privkeys] if pkid in
            kd]
        self._keys.pop(pkid)
        for m, a in [(m, a) for m in self._aliases for a, p in m.items() if
            p == pkid]:
            m.pop(a)
            if a in self:
                self._sort_alias(a)
        if key.is_primary:
            [self.unload(sk) for sk in key.subkeys.values()]