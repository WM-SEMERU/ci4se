def filter_wildcard(names, pattern):
    return tuple(name for name in names if fnmatch.fnmatch(name, pattern))