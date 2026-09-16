def _check_pattern_list(patterns, key, default=None):
    if not patterns:
        return default
    if isinstance(patterns, basestring):
        return [patterns]
    if isinstance(patterns, list):
        if all(isinstance(p, basestring) for p in patterns):
            return patterns
    raise ValueError(
        "Invalid file patterns in key '{}': must be a string or list of strings"
        .format(key))