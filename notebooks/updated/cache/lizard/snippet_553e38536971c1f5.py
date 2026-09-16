def _transform_cur_commands(cur_commands, alias_table=None):
    transformed = []
    alias_table = alias_table if alias_table else get_alias_table()
    for cmd in cur_commands:
        if cmd in alias_table.sections() and alias_table.has_option(cmd,
            'command'):
            transformed += alias_table.get(cmd, 'command').split()
        else:
            transformed.append(cmd)
    cur_commands[:] = transformed