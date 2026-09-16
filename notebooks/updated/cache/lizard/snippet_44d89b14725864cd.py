def parse_version_info(version):
    parts = parse(version)
    version_info = VersionInfo(parts['major'], parts['minor'], parts[
        'patch'], parts['prerelease'], parts['build'])
    return version_info