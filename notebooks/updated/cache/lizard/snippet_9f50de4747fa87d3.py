def match(self, filename, isdir):
    fnmatch = _fnmatch.fnmatch
    ignored = False
    filename = self.convert_path(filename)
    basename = os.path.basename(filename)
    for pattern in self.patterns:
        if pattern.dir_only and not isdir:
            continue
        if (not ignored or pattern.invert) and pattern.match(filename):
            if pattern.invert:
                return MATCH_INCLUDE
            ignored = True
    if ignored:
        return MATCH_IGNORE
    else:
        return MATCH_DEFAULT