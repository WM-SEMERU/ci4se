def get_command(self, ctx, cmd_name):
    rv = click.Group.get_command(self, ctx, cmd_name)
    if rv is not None:
        return rv
    cmd_name = self.command_aliases.get(cmd_name, '')
    return click.Group.get_command(self, ctx, cmd_name)