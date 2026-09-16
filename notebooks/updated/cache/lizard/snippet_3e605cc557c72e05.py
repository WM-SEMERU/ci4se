def convert_environment(datadir, version, always_yes):
    require_images()
    inp = None
    old_version = _get_current_format(datadir)
    migration_func = migrations[old_version, version]
    if version > CURRENT_FORMAT_VERSION:
        raise DatacatsError(
            'Cannot migrate to a version higher than the current one.')
    if version < 1:
        raise DatacatsError('Datadir versioning starts at 1.')
    if not always_yes:
        while inp != 'y' and inp != 'n':
            inp = raw_input(migration_func.__doc__.format(version))
        if inp == 'n':
            sys.exit(1)
    lockfile = LockFile(path_join(datadir, '.migration_lock'))
    lockfile.acquire()
    try:
        migration_func(datadir)
    finally:
        lockfile.release()