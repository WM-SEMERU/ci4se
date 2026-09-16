def initLogging():
    logging.basicConfig(level=logging.INFO, format=
        '%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(message)s',
        datefmt='%H:%M:%S')
    logging.getLogger('').setLevel(logging.INFO)
    logging.getLogger('PIL').setLevel(logging.INFO)
    CONFIG_PATHS = [os.path.curdir, os.path.join(os.path.expanduser('~')),
        '/etc']
    for p in CONFIG_PATHS:
        config_file = os.path.join(p, 'ocrd_logging.py')
        if os.path.exists(config_file):
            logging.info("Loading logging configuration from '%s'", config_file
                )
            with open(config_file) as f:
                code = compile(f.read(), config_file, 'exec')
                exec(code, globals(), locals())