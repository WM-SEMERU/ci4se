def run(command, show=True, *args, **kwargs):
    if show:
        print_command(command)
    with hide('running'):
        return _run(command, *args, **kwargs)