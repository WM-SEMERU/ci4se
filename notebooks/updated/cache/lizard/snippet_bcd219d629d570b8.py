def invoked_with(self):
    command_name = self._command_impl.name
    ctx = self.context
    if (ctx is None or ctx.command is None or ctx.command.qualified_name !=
        command_name):
        return command_name
    return ctx.invoked_with