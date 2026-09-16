def _apply_single(self, string):
    if string is None:
        return None
    result = self.trans_map.transliterate(string)
    result = self.SPACES_REGEX.sub(' ', result).strip()
    return result