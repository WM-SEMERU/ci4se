def init_app(self, app):
    config_log_level = app.config.get('FLASK_LOG_LEVEL', None)
    hostname = platform.node().split('.')[0]
    formatter = (
        '[%(asctime)s] %(levelname)s %(process)d [%(name)s] %(filename)s:%(lineno)d - [{hostname}] - %(message)s'
        .format(hostname=hostname))
    config_log_int = None
    set_level = None
    if config_log_level:
        config_log_int = getattr(logging, config_log_level.upper(), None)
        if not isinstance(config_log_int, int):
            raise ValueError('Invalid log level: {0}'.format(config_log_level))
        set_level = config_log_int
    if not set_level:
        set_level = config_log_int = logging.NOTSET
    self.log_level = set_level
    logging.basicConfig(format=formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(set_level)
    address = None
    if os.path.exists('/dev/log'):
        address = '/dev/log'
    elif os.path.exists('/var/run/syslog'):
        address = '/var/run/syslog'
    else:
        address = '127.0.0.1', 514
    root_logger.addHandler(SysLogHandler(address=address, facility=
        SysLogHandler.LOG_LOCAL0))
    self.set_formatter(formatter)
    return config_log_int