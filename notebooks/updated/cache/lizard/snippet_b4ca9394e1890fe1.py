def add_command(self, command):
    if not isinstance(command, Command):
        raise TypeError('The command passed must be a subclass of Command')
    if isinstance(self, Command):
        command.parent = self
    if command.name in self.all_commands:
        raise discord.ClientException('Command {0.name} is already registered.'
            .format(command))
    self.all_commands[command.name] = command
    for alias in command.aliases:
        if alias in self.all_commands:
            raise discord.ClientException(
                'The alias {} is already an existing command or alias.'.
                format(alias))
        self.all_commands[alias] = command