def _is_gpg1(version):
    major, minor, micro = _match_version_string(version)
    if major == 1:
        return True
    return False