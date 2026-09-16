def match_pattern(nm, patterns):
    patterns = coerce_to_list(patterns)
    for pat in patterns:
        if fnmatch.fnmatch(nm, pat):
            return True
    return False