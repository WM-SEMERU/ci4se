def create_handler(target: str):
    if target == 'stderr':
        return logging.StreamHandler(sys.stderr)
    elif target == 'stdout':
        return logging.StreamHandler(sys.stdout)
    else:
        return logging.handlers.WatchedFileHandler(filename=target)