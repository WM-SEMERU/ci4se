def match(command, options, args):
    build = ''
    possible = commands
    for l in command:
        build += l
        possible = filter(lambda w: w.startswith(build), possible)
    if len(possible) == 0:
        raise ArgError('Command invalid: %s' % command)
    if len(possible) > 1:
        raise ArgError('Ambiguous command: %s' % command)
    command = possible.pop()
    if not num_args[command](len(args)):
        raise ArgError('Bad number of args for command %s' % command)
    return command