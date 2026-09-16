def encode_exception(exception):
    import sys
    return AsyncException(unicode(exception), exception.args, sys.exc_info(
        ), exception)