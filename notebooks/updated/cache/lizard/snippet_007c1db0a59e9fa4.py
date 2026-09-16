def dispatch(args):
    prog_name = args[0]
    if prog_name not in dispatchers:
        raise NoSuchScriptError('No such pyokit script: ' + prog_name + '\n')
    else:
        dispatchers[prog_name](args[1:])