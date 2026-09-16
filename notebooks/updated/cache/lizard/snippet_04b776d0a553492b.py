def fnmatches(entry, *pattern_list):
    for pattern in pattern_list:
        if pattern and fnmatch(entry, pattern):
            return True
    return False