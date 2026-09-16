def is_a_tty(stream=sys.stdout):
    result = stream.isatty() if hasattr(stream, 'isatty') else None
    log.debug(result)
    return result