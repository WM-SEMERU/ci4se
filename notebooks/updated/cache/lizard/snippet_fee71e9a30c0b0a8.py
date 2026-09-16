def process_casperjs_stdout(stdout):
    for line in stdout.splitlines():
        bits = line.split(':', 1)
        if len(bits) < 2:
            bits = 'INFO', bits
        level, msg = bits
        if level == 'FATAL':
            logger.fatal(msg)
            raise CaptureError(msg)
        elif level == 'ERROR':
            logger.error(msg)
        else:
            logger.info(msg)