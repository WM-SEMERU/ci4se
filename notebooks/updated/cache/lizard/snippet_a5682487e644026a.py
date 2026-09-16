def _FindKeys(self, key, names, matches):
    for name, subkey in iter(key.items()):
        if name in names:
            matches.append((name, subkey))
        if isinstance(subkey, dict):
            self._FindKeys(subkey, names, matches)