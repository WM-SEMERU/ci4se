def coerce(cls, version_string, partial=False):
    base_re = re.compile('^\\d+(?:\\.\\d+(?:\\.\\d+)?)?')
    match = base_re.match(version_string)
    if not match:
        raise ValueError('Version string lacks a numerical component: %r' %
            version_string)
    version = version_string[:match.end()]
    if not partial:
        while version.count('.') < 2:
            version += '.0'
    if match.end() == len(version_string):
        return Version(version, partial=partial)
    rest = version_string[match.end():]
    rest = re.sub('[^a-zA-Z0-9+.-]', '-', rest)
    if rest[0] == '+':
        prerelease = ''
        build = rest[1:]
    elif rest[0] == '.':
        prerelease = ''
        build = rest[1:]
    elif rest[0] == '-':
        rest = rest[1:]
        if '+' in rest:
            prerelease, build = rest.split('+', 1)
        else:
            prerelease, build = rest, ''
    elif '+' in rest:
        prerelease, build = rest.split('+', 1)
    else:
        prerelease, build = rest, ''
    build = build.replace('+', '.')
    if prerelease:
        version = '%s-%s' % (version, prerelease)
    if build:
        version = '%s+%s' % (version, build)
    return cls(version, partial=partial)