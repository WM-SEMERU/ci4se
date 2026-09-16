def _release_line(c):
    branch = c.run('git rev-parse --abbrev-ref HEAD', hide=True).stdout.strip()
    type_ = Release.UNDEFINED
    if BUGFIX_RE.match(branch):
        type_ = Release.BUGFIX
    if FEATURE_RE.match(branch):
        type_ = Release.FEATURE
    return branch, type_