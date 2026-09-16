def filter_paths(pathnames, patterns=None, ignore_patterns=None):
    result = []
    if patterns is None:
        patterns = ['*']
    if ignore_patterns is None:
        ignore_patterns = []
    for pathname in pathnames:
        if match_patterns(pathname, patterns) and not match_patterns(pathname,
            ignore_patterns):
            result.append(pathname)
    return result