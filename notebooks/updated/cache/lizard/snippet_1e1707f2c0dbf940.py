def print_verbose(*args, **kwargs):
    if kwargs.pop('verbose', False) is True:
        gprint(*args, **kwargs)