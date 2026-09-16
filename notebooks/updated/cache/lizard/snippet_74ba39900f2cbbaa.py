def command_with_options(self):
    if 'args' in self.config:
        return ' '.join((self.command, self.config['args']))
    return self.command