def fast_relpath_optional(path, start):
    if len(start) == 0:
        return path
    pref_end = len(start) - 1 if start[-1] == '/' else len(start)
    if pref_end > len(path):
        return None
    elif path[:pref_end] == start[:pref_end] and (len(path) == pref_end or 
        path[pref_end] == '/'):
        return path[pref_end + 1:]