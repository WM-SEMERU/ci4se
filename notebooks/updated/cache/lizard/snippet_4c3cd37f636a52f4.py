def add_command(self, command):
    self._commands.append(command)
    self._build_command_chain(command)