def filter(self, key_pattern='*', is_regex=False):
    if is_regex:
        if isinstance(key_pattern, str):
            regex = re.compile(key_pattern)
        else:
            regex = key_pattern
    else:
        regex = None
    for k, v in self.items():
        if regex and regex.match(k) or not regex and fnmatch(k, key_pattern):
            yield k, v