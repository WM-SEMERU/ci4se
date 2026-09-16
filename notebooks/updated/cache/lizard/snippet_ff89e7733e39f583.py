def get_pkg_version(pkg_name, parse=False):
    import pkg_resources
    try:
        version = pkg_resources.require(pkg_name)[0].version
        return pkg_resources.parse_version(version) if parse else version
    except pkg_resources.DistributionNotFound:
        return None