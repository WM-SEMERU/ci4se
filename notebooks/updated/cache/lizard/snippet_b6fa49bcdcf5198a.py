def get_packagers_of_package(config, package):
    if not _cache.is_configured:
        _cache.configure(**config['fmn.rules.cache'])
    key = cache_key_generator(get_packagers_of_package, package)
    creator = lambda : _get_pkgdb2_packagers_for(config, package)
    return _cache.get_or_create(key, creator)