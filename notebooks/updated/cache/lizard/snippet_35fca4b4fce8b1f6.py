def load_arguments(self, command):
    from knack.arguments import ArgumentsContext
    self.cli_ctx.raise_event(EVENT_CMDLOADER_LOAD_ARGUMENTS, cmd_tbl=self.
        command_table, command=command)
    try:
        self.command_table[command].load_arguments()
    except KeyError:
        return
    with ArgumentsContext(self, '') as c:
        c.ignore('cmd')
    self._apply_parameter_info(command, self.command_table[command])