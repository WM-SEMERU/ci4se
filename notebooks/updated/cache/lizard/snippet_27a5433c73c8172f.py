def exclude(self, pattern):
    match = translate_pattern(pattern)
    return self._remove_files(match.match)