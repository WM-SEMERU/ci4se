def list_upgrades(refresh=True, **kwargs):
    pkgs = {}
    for pkg in sorted(list_pkgs(refresh=refresh).keys()):
        pkg_upgrade = latest_version(pkg, refresh=False)
        if pkg_upgrade:
            pkgs[pkg] = pkg_upgrade
    return pkgs