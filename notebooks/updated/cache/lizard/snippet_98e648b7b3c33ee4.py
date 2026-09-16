def init_console_logging(conf):
    console = find_console_handler(logging.getLogger())
    if not console:
        console = logging.StreamHandler()
    logging_level = log_level(conf)
    console.setLevel(logging_level)
    formatter = _get_debug_formatter(conf)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(logging_level)
    global LOG
    LOG = logging.getLogger(__name__)