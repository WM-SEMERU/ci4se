def err(msg, level=-1, prefix=True):
    if will_print(level) or verbosity is None:
        printer(('ERROR: ' if prefix else '') + msg, 'red')