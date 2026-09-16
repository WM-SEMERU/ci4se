def get_commands_in_namespace(namespace=None, level=1):
    from ..command import Command
    commands = {}
    if namespace is None:
        frame = inspect.stack()[level][0]
        namespace = frame.f_globals
    elif inspect.ismodule(namespace):
        namespace = vars(namespace)
    for name in namespace:
        obj = namespace[name]
        if isinstance(obj, Command):
            commands[name] = obj
    return OrderedDict((name, commands[name]) for name in sorted(commands))