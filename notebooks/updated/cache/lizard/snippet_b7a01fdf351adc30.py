def detect_log_config(arguments):
    config = arguments['--config']
    if config is None:
        config = detect_config_path()
    if not os.path.exists(config):
        error_exit('Nginx config file not found: %s' % config)
    with open(config) as f:
        config_str = f.read()
    access_logs = dict(get_access_logs(config_str))
    if not access_logs:
        error_exit(
            'Access log file is not provided and ngxtop cannot detect it from your config file (%s).'
             % config)
    log_formats = dict(get_log_formats(config_str))
    if len(access_logs) == 1:
        log_path, format_name = list(access_logs.items())[0]
        if format_name == 'combined':
            return log_path, LOG_FORMAT_COMBINED
        if format_name not in log_formats:
            error_exit(
                'Incorrect format name set in config for access log file "%s"'
                 % log_path)
        return log_path, log_formats[format_name]
    print('Multiple access logs detected in configuration:')
    log_path = choose_one(list(access_logs.keys()),
        'Select access log file to process: ')
    format_name = access_logs[log_path]
    if format_name not in log_formats:
        error_exit(
            'Incorrect format name set in config for access log file "%s"' %
            log_path)
    return log_path, log_formats[format_name]