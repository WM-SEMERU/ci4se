def log_info(msg, logger='TaskLogger'):
    tasklogger = get_tasklogger(logger)
    tasklogger.info(msg)
    return tasklogger