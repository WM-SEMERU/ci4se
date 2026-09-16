def getDigestableArgs(Argv):
    r
    first_kwarg_pos = 0
    for arg in Argv:
        if KWARG_VALIDATOR.search(arg):
            break
        else:
            first_kwarg_pos += 1
    for arg in Argv[first_kwarg_pos:]:
        if not KWARG_VALIDATOR.search(arg):
            raise HandledException('Could not parse the arg "%s".' % arg)
    return Argv[:first_kwarg_pos], list2dict(Argv[first_kwarg_pos:])