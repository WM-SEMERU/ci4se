def fetch_command(self, subcommand):
    commands = get_commands()
    try:
        app_name = commands[subcommand]
    except KeyError:
        settings.INSTALLED_APPS
        sys.stderr.write("Unknown command: %r\nType '%s help' for usage.\n" %
            (subcommand, self.prog_name))
        sys.exit(1)
    if isinstance(app_name, BaseCommand):
        klass = app_name
    else:
        klass = load_command_class(app_name, subcommand)
    return klass