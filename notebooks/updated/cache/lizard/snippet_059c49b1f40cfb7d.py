def init_logging(log_level):
    log_level = log_level_to_string_map[min(log_level, 5)]
    msg = ('%(levelname)s - %(name)s:%(lineno)s - %(message)s' if log_level in
        os.environ else '%(levelname)s - %(message)s')
    logging_conf = {'version': 1, 'root': {'level': log_level, 'handlers':
        ['console']}, 'handlers': {'console': {'class':
        'logging.StreamHandler', 'level': log_level, 'formatter': 'simple',
        'stream': 'ext://sys.stdout'}}, 'formatters': {'simple': {'format':
        ' {0}'.format(msg)}}}
    logging.config.dictConfig(logging_conf)