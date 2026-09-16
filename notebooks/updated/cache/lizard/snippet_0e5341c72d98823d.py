def command(self, command, value=1, callback=None, check=True,
    allowable_errors=[], **kwargs):
    if isinstance(command, basestring):
        command = SON([(command, value)])
    command.update(kwargs)
    self.connection('$cmd').find_one(command, callback=callback,
        _must_use_master=True, _is_command=True)