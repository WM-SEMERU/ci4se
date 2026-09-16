def execute_flow(self, custom_command='', is_config=False):
    responses = []
    if isinstance(custom_command, str):
        commands = [custom_command]
    elif isinstance(custom_command, tuple):
        commands = list(custom_command)
    else:
        commands = custom_command
    if is_config:
        mode = self._cli_handler.config_mode
        if not mode:
            raise Exception(self.__class__.__name__,
                'CliHandler configuration is missing. Config Mode has to be defined'
                )
    else:
        mode = self._cli_handler.enable_mode
        if not mode:
            raise Exception(self.__class__.__name__,
                'CliHandler configuration is missing. Enable Mode has to be defined'
                )
    with self._cli_handler.get_cli_service(mode) as session:
        for cmd in commands:
            responses.append(session.send_command(command=cmd))
    return '\n'.join(responses)