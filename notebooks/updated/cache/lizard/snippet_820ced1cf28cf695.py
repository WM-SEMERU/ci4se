def run(self, command, arguments=(), console_mode_stdin=True,
    skip_cmd_shell=False):
    logging.info('running command: ' + command)
    resource = ResourceLocator(CommandShell.ShellResource)
    resource.add_selector('ShellId', self.__shell_id)
    resource.add_option('WINRS_SKIP_CMD_SHELL', ['FALSE', 'TRUE'][bool(
        skip_cmd_shell)], True)
    resource.add_option('WINRS_CONSOLEMODE_STDIN', ['FALSE', 'TRUE'][bool(
        console_mode_stdin)], True)
    command = OrderedDict([('rsp:Command', command)])
    command['rsp:Arguments'] = list(arguments)
    response = self.session.command(resource, {'rsp:CommandLine': command})
    command_id = response['rsp:CommandResponse']['rsp:CommandId']
    logging.info('receive command: ' + command_id)
    return command_id