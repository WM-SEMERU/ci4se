def run_command(self, commands):
    self.vsctl.run_command(commands, self.timeout, self.exception)