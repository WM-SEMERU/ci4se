def collect_commands(package_name=None, in_place=False, level=1):
    commands = {}
    frame = inspect.stack()[level][0]
    f_globals = frame.f_globals
    if package_name is None:
        package_name = f_globals['__name__'].rsplit('.', 1)[0]
        package_paths = [os.path.dirname(f_globals['__file__'])]
    else:
        package = importlib.import_module(package_name)
        package_name = package.__name__
        package_paths = package.__path__
    for package_path in package_paths:
        package_path = pathlib.Path(package_path)
        for file in package_path.rglob('*.py'):
            rel_path = str(file.relative_to(package_path))
            rel_path = rel_path[:-3]
            module_name = rel_path.replace(os.sep, '.')
            module_name = '.'.join((package_name, module_name))
            module = importlib.import_module(module_name)
            module_commands = get_commands_in_namespace(module)
            commands.update(module_commands)
    commands = OrderedDict((name, commands[name]) for name in sorted(commands))
    if in_place:
        f_globals.update(commands)
    return commands