def strip_sdist_extras(filelist):
    return [name for name in filelist if not file_matches(name, IGNORE) and
        not file_matches_regexps(name, IGNORE_REGEXPS)]