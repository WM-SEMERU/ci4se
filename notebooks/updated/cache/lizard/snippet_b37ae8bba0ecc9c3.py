def check_valid_package(package, cyg_arch='x86_64', mirrors=None):
    if mirrors is None:
        mirrors = [{DEFAULT_MIRROR: DEFAULT_MIRROR_KEY}]
    LOG.debug('Checking Valid Mirrors: %s', mirrors)
    for mirror in mirrors:
        for mirror_url, key in mirror.items():
            if package in _get_all_packages(mirror_url, cyg_arch):
                return True
    return False