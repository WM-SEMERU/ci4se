def get_swift_codename(version):
    codenames = [k for k, v in six.iteritems(SWIFT_CODENAMES) if version in v]
    if len(codenames) > 1:
        for codename in reversed(codenames):
            releases = UBUNTU_OPENSTACK_RELEASE
            release = [k for k, v in six.iteritems(releases) if codename in v]
            ret = subprocess.check_output(['apt-cache', 'policy', 'swift'])
            if six.PY3:
                ret = ret.decode('UTF-8')
            if codename in ret or release[0] in ret:
                return codename
    elif len(codenames) == 1:
        return codenames[0]
    match = re.match('^(\\d+)\\.(\\d+)', version)
    if match:
        major_minor_version = match.group(0)
        for codename, versions in six.iteritems(SWIFT_CODENAMES):
            for release_version in versions:
                if release_version.startswith(major_minor_version):
                    return codename
    return None