def get_command_signature(self, command):
    parent = command.full_parent_name
    if len(command.aliases) > 0:
        aliases = '|'.join(command.aliases)
        fmt = '[%s|%s]' % (command.name, aliases)
        if parent:
            fmt = parent + ' ' + fmt
        alias = fmt
    else:
        alias = command.name if not parent else parent + ' ' + command.name
    return '%s%s %s' % (self.clean_prefix, alias, command.signature)