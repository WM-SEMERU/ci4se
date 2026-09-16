def config(self, commands, **kwargs):
    commands = make_iterable(commands)
    commands = list(commands)
    commands.insert(0, 'configure terminal')
    response = self.run_commands(commands, **kwargs)
    if self.autorefresh:
        self.refresh()
    response.pop(0)
    return response