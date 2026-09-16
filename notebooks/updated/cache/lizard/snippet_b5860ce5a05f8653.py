def subliminal(ctx, addic7ed, legendastv, opensubtitles, subscenter,
    cache_dir, debug):
    try:
        os.makedirs(cache_dir)
    except OSError:
        if not os.path.isdir(cache_dir):
            raise
    region.configure('dogpile.cache.dbm', expiration_time=timedelta(days=30
        ), arguments={'filename': os.path.join(cache_dir, cache_file),
        'lock_factory': MutexLock})
    if debug:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
        logging.getLogger('subliminal').addHandler(handler)
        logging.getLogger('subliminal').setLevel(logging.DEBUG)
    ctx.obj = {'provider_configs': {}}
    if addic7ed:
        ctx.obj['provider_configs']['addic7ed'] = {'username': addic7ed[0],
            'password': addic7ed[1]}
    if legendastv:
        ctx.obj['provider_configs']['legendastv'] = {'username': legendastv
            [0], 'password': legendastv[1]}
    if opensubtitles:
        ctx.obj['provider_configs']['opensubtitles'] = {'username':
            opensubtitles[0], 'password': opensubtitles[1]}
    if subscenter:
        ctx.obj['provider_configs']['subscenter'] = {'username': subscenter
            [0], 'password': subscenter[1]}