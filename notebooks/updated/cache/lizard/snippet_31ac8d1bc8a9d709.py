def walk_commands(self):
    for command in tuple(self.all_commands.values()):
        yield command
        if isinstance(command, GroupMixin):
            yield from command.walk_commands()