def _stacklevel_above_module(mod_name):
    stacklevel = 2
    frame = inspect.stack()[stacklevel][0]
    while True:
        if frame.f_globals.get('__name__', None) != mod_name:
            break
        stacklevel += 1
        frame = frame.f_back
    del frame
    return stacklevel