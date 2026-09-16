def verify_weave_options(opt, parser):
    cache_dir = os.environ['PYTHONCOMPILED']
    if opt.fixed_weave_cache:
        if os.environ.get('FIXED_WEAVE_CACHE', None):
            cache_dir = os.environ['FIXED_WEAVE_CACHE']
        elif getattr(sys, 'frozen', False):
            cache_dir = sys._MEIPASS
        else:
            cache_dir = os.path.join(os.getcwd(), 'pycbc_inspiral')
        os.environ['PYTHONCOMPILED'] = cache_dir
        logging.debug('fixed_weave_cache: Setting weave cache to %s', cache_dir
            )
        sys.path = [cache_dir] + sys.path
        try:
            os.makedirs(cache_dir)
        except OSError:
            pass
        if not os.environ.get('LAL_DATA_PATH', None):
            os.environ['LAL_DATA_PATH'] = cache_dir
    if opt.per_process_weave_cache:
        cache_dir = os.path.join(cache_dir, str(os.getpid()))
        os.environ['PYTHONCOMPILED'] = cache_dir
        logging.info('Setting weave cache to %s', cache_dir)
    if not os.path.exists(cache_dir):
        try:
            os.makedirs(cache_dir)
        except:
            logging.error('Unable to create weave cache %s', cache_dir)
            sys.exit(1)
    if opt.clear_weave_cache_at_start:
        _clear_weave_cache()
        os.makedirs(cache_dir)
    if opt.clear_weave_cache_at_end:
        atexit.register(_clear_weave_cache)
        signal.signal(signal.SIGTERM, _clear_weave_cache)