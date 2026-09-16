def normalize_pattern(pattern):
    if not (pattern.startswith('RE:') or pattern.startswith('!RE:')):
        pattern = _slashes.sub('/', pattern)
    if len(pattern) > 1:
        pattern = pattern.rstrip('/')
    return pattern