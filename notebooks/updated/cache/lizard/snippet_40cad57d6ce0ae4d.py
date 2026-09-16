def get_command(self, ctx, cmd_name):
    cmd_name = self.MAP.get(cmd_name, cmd_name)
    return super(AliasedGroup, self).get_command(ctx, cmd_name)