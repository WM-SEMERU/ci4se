def main(name, klass):
    parser = create_args_parser(name)
    cargs = get_common_args(parser)
    logging.getLogger().setLevel(cargs['log_level'])
    wrapper = klass(certfile=cargs['certfile'], keyfile=cargs['keyfile'],
        cafile=cargs['cafile'])
    if cargs['version']:
        print_version(wrapper)
        sys.exit()
    if cargs['foreground']:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter(
            '%(asctime)s %(name)s: %(levelname)s: %(message)s'))
        logging.getLogger().addHandler(console)
    elif cargs['log_file']:
        logfile = logging.handlers.WatchedFileHandler(cargs['log_file'])
        logfile.setFormatter(logging.Formatter(
            '%(asctime)s %(name)s: %(levelname)s: %(message)s'))
        logging.getLogger().addHandler(logfile)
        go_to_background()
    else:
        syslog = logging.handlers.SysLogHandler('/dev/log')
        syslog.setFormatter(logging.Formatter(
            '%(name)s: %(levelname)s: %(message)s'))
        logging.getLogger().addHandler(syslog)
        syslog_fd = syslog.socket.fileno()
        os.dup2(syslog_fd, 1)
        os.dup2(syslog_fd, 2)
        go_to_background()
    if not wrapper.check():
        return 1
    return wrapper.run(cargs['address'], cargs['port'], cargs['unix_socket'])