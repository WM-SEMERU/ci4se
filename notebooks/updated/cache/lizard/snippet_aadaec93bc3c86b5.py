def subkey(self, i=0, is_hardened=False, as_private=None):
    if as_private is None:
        as_private = self.secret_exponent() is not None
    is_hardened = not not is_hardened
    as_private = not not as_private
    lookup = i, is_hardened, as_private
    if lookup not in self._subkey_cache:
        self._subkey_cache[lookup] = self._subkey(i, is_hardened, as_private)
    return self._subkey_cache[lookup]