def is_upload(action):
    return 'r' in action.type._mode and (action.default is None or getattr(
        action.default, 'name') not in (sys.stderr.name, sys.stdout.name))