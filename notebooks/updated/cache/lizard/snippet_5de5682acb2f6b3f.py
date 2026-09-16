def _apply_single(self, string):
    if string is None:
        return None
    result = self.regex.sub('', string)
    result = self.SPACES_REGEX.sub(' ', result).strip()
    return result