def build_command(self):
    if self.options['command']:
        return self.options['command'](self) if callable(self.options[
            'command']) else self.options['command']
    return self.build_default_command()