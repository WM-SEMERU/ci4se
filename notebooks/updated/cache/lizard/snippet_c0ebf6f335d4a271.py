def _nargs_validator(nargs, message):
    if message is None:
        message = 'Registered function must take exactly %d arguments' % nargs

    def f(key, value):
        del key
        spec = inspect.getfullargspec(value)
        if len(spec.args
            ) != nargs or spec.varargs is not None or spec.varkw is not None:
            raise ValueError(message)
    return f