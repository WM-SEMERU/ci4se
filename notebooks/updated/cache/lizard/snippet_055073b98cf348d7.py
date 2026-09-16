def pattern_to_str(pattern):
    if isinstance(pattern, str):
        return repr(pattern)
    else:
        return repr(pattern.pattern) if pattern else None