def configure_logging(conf):
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, conf.loglevel.upper()))
    if conf.logtostderr:
        add_stream_handler(root_logger, sys.stderr)
    if conf.logtostdout:
        add_stream_handler(root_logger, sys.stdout)