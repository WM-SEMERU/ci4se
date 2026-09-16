def configure(paths, relative_to):
    if not paths:
        return
    for path in [normalize_path(p, relative_to) for p in paths]:
        logger.debug('configuration path {0}'.format(path))
        pubkeys_path = join(path, PUBKEYSDIR)
        if os.path.exists(pubkeys_path):
            load_pubkeys(pubkeys_path, PUBKEYS)
        init_module(path)