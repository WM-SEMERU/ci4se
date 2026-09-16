def distribution_compatible(dist, supported_tags=None):
    if supported_tags is None:
        supported_tags = get_supported()
    package = Package.from_href(dist.location)
    if not package:
        return False
    return package.compatible(supported_tags)