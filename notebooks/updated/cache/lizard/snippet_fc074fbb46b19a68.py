def setup_logging(level, console_stream=None, log_dir=None, scope=None,
    log_name=None, native=None):
    log_filename = None
    file_handler = None

    def trace(self, message, *args, **kwargs):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, message, args, **kwargs)
    logging.Logger.trace = trace
    logger = logging.getLogger(scope)
    for handler in logger.handlers:
        logger.removeHandler(handler)
    if console_stream:
        native_handler = create_native_stderr_log_handler(level, native,
            stream=console_stream)
        logger.addHandler(native_handler)
    if log_dir:
        safe_mkdir(log_dir)
        log_filename = os.path.join(log_dir, log_name or 'pants.log')
        native_handler = create_native_pantsd_file_log_handler(level,
            native, log_filename)
        file_handler = native_handler
        logger.addHandler(native_handler)
    logger.setLevel(level)
    logging.captureWarnings(True)
    _maybe_configure_extended_logging(logger)
    return LoggingSetupResult(log_filename, file_handler)