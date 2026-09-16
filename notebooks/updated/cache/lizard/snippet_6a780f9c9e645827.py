def fitString(s, maxCol=79, newlineReplacement=None):
    r
    assert isString(s)
    if '\n' in s:
        if newlineReplacement is None:
            s = s[:s.index('\n')]
        else:
            s = s.replace('\n', newlineReplacement)
    if maxCol is not None and len(s) > maxCol:
        s = '%s...' % s[:maxCol - 3]
    return s