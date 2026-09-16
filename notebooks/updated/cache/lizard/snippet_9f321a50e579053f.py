def format_exc(*exc_info):
    typ, exc, tb = exc_info or sys.exc_info()
    error = traceback.format_exception(typ, exc, tb)
    return ''.join(error)