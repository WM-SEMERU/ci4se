def is_ssl_error(error=None):
    exc_types = ssl.SSLError,
    try:
        from OpenSSL.SSL import Error
        exc_types += Error,
    except ImportError:
        pass
    if error is None:
        error = sys.exc_info()[1]
    return isinstance(error, exc_types)