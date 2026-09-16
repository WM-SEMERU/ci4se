def _configure_logging(verbose=False, debug=False):
    overall_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format=
        '{levelname[0]}{asctime}.{msecs:03.0f} {thread} {filename}:{lineno}] {message}'
        , datefmt='%m%d %H:%M:%S', style='{', level=overall_level)
    global log
    log = logging.getLogger('portserver')
    log.setLevel(logging.DEBUG if verbose else overall_level)