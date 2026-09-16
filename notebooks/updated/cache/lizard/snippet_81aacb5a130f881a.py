def do(self, command):
    echo = self.echo and command or ''
    if not self.logged_in:
        return echo + '\n' + self._get_prompt()
    response = self.commands.eval(command)
    if response is None:
        return echo + '\n' + self._get_prompt()
    return echo + response