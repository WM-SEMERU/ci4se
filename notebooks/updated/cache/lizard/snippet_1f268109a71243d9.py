def validateMasterArgument(self, master_arg):
    if master_arg[:5] == 'http:':
        raise usage.UsageError('<master> is not a URL - do not use URL')
    if ':' not in master_arg:
        master = master_arg
        port = 9989
    else:
        master, port = master_arg.split(':')
    if not master:
        raise usage.UsageError("invalid <master> argument '{}'".format(
            master_arg))
    try:
        port = int(port)
    except ValueError:
        raise usage.UsageError("invalid master port '{}', needs to be a number"
            .format(port))
    return master, port