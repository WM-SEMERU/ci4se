def log_every_n(level, msg, n, *args):
    count = _get_next_log_count_per_token(get_absl_logger().findCaller())
    log_if(level, msg, not count % n, *args)