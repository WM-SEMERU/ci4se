def log_to_syslog():
    rl = logging.getLogger()
    rl.setLevel('INFO')
    stderr = logging.StreamHandler(stream=sys.stderr)
    stderr.setLevel(logging.CRITICAL)
    stderr.setFormatter(logging.Formatter(
        '%(asctime)s %(name)s: %(levelname)s %(message)s'))
    rl.addHandler(stderr)
    syslog = SysLogHandler(address='/dev/log', facility=SysLogHandler.LOG_MAIL)
    syslog.setFormatter(logging.Formatter(
        '%(name)s[%(process)d]: %(levelname)s %(message)s'))
    rl.addHandler(syslog)