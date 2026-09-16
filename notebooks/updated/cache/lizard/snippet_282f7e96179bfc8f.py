def _get_parser(self, env):
    version_str = 'focus version ' + __version__
    usage_str = 'focus [-h] [-v] [--no-color] <command> [<args>]'
    parser = FocusArgParser(description=
        'Command-line productivity tool for improved task workflows.',
        epilog=
        "See 'focus help <command>' for more information on a specific command."
        , usage=usage_str)
    parser.add_argument('-v', '--version', action='version', version=
        version_str)
    parser.add_argument('--no-color', action='store_true', help=
        'disables colors')
    commands = []
    active = env.task.active
    command_hooks = registration.get_registered(command_hooks=True,
        task_active=active)
    for plugin in command_hooks:
        help_text = (plugin.__doc__ or '').strip().rstrip('.').lower()
        commands.append((plugin.command, help_text))
    commands.sort(key=lambda x: x[0])
    subparsers = parser.add_subparsers(title='available commands')
    help_parser = subparsers.add_parser('help', add_help=False)
    help_parser.set_defaults(func=self._handle_help)
    version_parser = subparsers.add_parser('version', add_help=False)

    def _print_version(env, args):
        env.io.write(version_str)
        return True
    version_parser.set_defaults(func=_print_version)
    for command, help_ in commands:
        cmd_parser = subparsers.add_parser(command, help=help_, add_help=False)

        def _run(command):

            def _wrapper(env, args):
                return self._handle_command(command, env, args)
            return _wrapper
        cmd_parser.set_defaults(func=_run(command))
    return parser