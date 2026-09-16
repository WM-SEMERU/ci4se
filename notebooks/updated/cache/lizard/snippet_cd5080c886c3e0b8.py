def CanonicalPathToLocalPath(path):
    r
    path = path.replace('/\\', '\\')
    path = path.replace('/', '\\')
    m = re.match('\\\\([a-zA-Z]):(.*)$', path)
    if m:
        path = '%s:\\%s' % (m.group(1), m.group(2).lstrip('\\'))
    return path