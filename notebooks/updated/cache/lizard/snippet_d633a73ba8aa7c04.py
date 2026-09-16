def help(self, *arg, **kwargs):
    try:
        name = arg[0]
    except IndexError:
        return 'welcome to vexbot! !commands will list all availabe commands'
    if any([name.startswith(x) for x in self._prompt.shebangs]):
        name = name[1:]
    try:
        callback = self._commands[name]
    except KeyError:
        self.logger.info(' !help not found for: %s', name)
        return self.help.__doc__
    return callback.__doc__