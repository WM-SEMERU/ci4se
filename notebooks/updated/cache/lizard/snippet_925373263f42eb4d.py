def description(self, platform, key):
    patterns = self._dict_dscr.get(platform, None)
    description = patterns.get(key, None)
    return description