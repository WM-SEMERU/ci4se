def respond_to_SIGHUP(signal_number, frame, logger=None):
    global restart
    restart = True
    if logger:
        logger.info('detected SIGHUP')
    raise KeyboardInterrupt