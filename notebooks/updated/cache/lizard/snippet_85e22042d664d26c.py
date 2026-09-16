def pkg_available(pkg_name, required=False):
    if pkg_name in pkgs:
        return True
    if required:
        nl.notify('Error: could not find required analysis package %s' %
            pkg_name, level=nl.level.error)
    return False