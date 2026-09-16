def commands(self):
    self._commands, value = self.get_attr_set(self._commands, 'commands')
    return value