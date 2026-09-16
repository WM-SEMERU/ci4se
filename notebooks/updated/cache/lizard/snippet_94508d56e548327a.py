def formatExcept(cls, error, trace):
    clsname = cls.__name__ if cls else 'UnknownError'
    tb = 'Traceback (most recent call last):\n'
    tb += ''.join(traceback.format_tb(trace))
    tb += '{0}: {1}'.format(clsname, error)
    return tb