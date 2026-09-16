def register_command_runner(arg):
    if isinstance(arg, str):

        def inner(command_runner):
            command_runners.setdefault(arg, [])
            command_runners[arg].append(command_runner)
            return command_runner
        return inner
    elif issubclass(arg, CommandRunner):
        command_runners.setdefault('', [])
        command_runners[''].append(arg)
        return arg
    else:
        msg = (
            'register_command_runner expects str or CommandRunner as argument, got: {0}'
            .format(arg))
        raise ValueError(msg)