def configure():
    root_logger = logging.getLogger()
    root_logger.addHandler(logging.NullHandler())
    root_logger.setLevel(99)
    _display_logger.setLevel(70)
    _debug_logger.setLevel(10)
    display_handlers = [h.get_name() for h in _display_logger.handlers]
    if 'stdout' not in display_handlers:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.set_name('stdout')
        formatter = logging.Formatter('%(message)s')
        stdout_handler.setFormatter(formatter)
        _display_logger.addHandler(stdout_handler)