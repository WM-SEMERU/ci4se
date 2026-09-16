def get_commands(self, namespace):
    if not namespace:
        namespace = DEFAULT_NAMESPACE
    try:
        namespace.strip().lower()
        commands = list(self._commands[namespace].keys())
        commands.sort()
        return commands
    except KeyError:
        return []