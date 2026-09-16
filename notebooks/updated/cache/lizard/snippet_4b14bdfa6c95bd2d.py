def substitute_filename(fn, variables):
    for var, value in variables.items():
        fn = fn.replace('+%s+' % var, str(value))
    return fn