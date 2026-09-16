def register_commands(self):
    for command in self._entry_points[self.COMMANDS_ENTRY_POINT].values():
        command.load()