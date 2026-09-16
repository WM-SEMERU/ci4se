def unregister(self, command):
    if command not in self._commands.keys():
        self.log.warning('Can not unregister command %s' % command)
    else:
        del self._click_root_command.commands[command]
        del self._commands[command]
        self.log.debug('Command %s got unregistered' % command)