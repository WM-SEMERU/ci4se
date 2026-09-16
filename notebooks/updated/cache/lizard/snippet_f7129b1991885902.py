def get_logger(file=None, syslog=False, loghost=None, level=None):
    if not syslog:
        if not file:
            handler = logging.StreamHandler(sys.stdout)
        else:
            handler = logging.FileHandler(file)
    elif loghost:
        handler = logging.handlers.SysLogHandler(loghost, 514)
    else:
        handler = logging.handlers.SysLogHandler()
    root_logger = logging.getLogger()
    if level:
        level = level.upper()
        lldict = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING':
            logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.
            CRITICAL}
        if level in lldict:
            root_logger.setLevel(lldict[level])
    root_logger.addHandler(handler)
    structlog.configure(processors=[structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name, structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(), structlog.
        processors.TimeStamper(fmt='iso'), structlog.processors.
        StackInfoRenderer(), structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()], context_class=structlog.
        threadlocal.wrap_dict(dict), logger_factory=structlog.stdlib.
        LoggerFactory(), wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True)
    log = structlog.get_logger()
    return log