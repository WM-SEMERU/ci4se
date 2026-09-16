def init_logging(logfile=None, loglevel=logging.INFO, configfile=None):
    use_configfile = False
    if configfile and os.path.exists(configfile):
        testcfg = ConfigParser()
        read = testcfg.read(configfile)
        use_configfile = read and testcfg.has_section('loggers')
    if use_configfile:
        logging.config.fileConfig(configfile)
        if logfile:
            msg = (
                'Config file conflicts with explicitly specified logfile; config file takes precedence.'
                )
            logging.warn(msg)
    else:
        format = (
            '%(asctime)s [%(threadName)s] %(name)s - %(levelname)s - %(message)s'
            )
        if logfile:
            logging.basicConfig(filename=logfile, level=loglevel, format=format
                )
        else:
            logging.basicConfig(level=loglevel, format=format)