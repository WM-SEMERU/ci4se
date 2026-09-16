def list_alias():
    alias_table = get_alias_table()
    output = []
    for alias in alias_table.sections():
        if alias_table.has_option(alias, 'command'):
            output.append({'alias': alias, 'command': ' '.join(alias_table.
                get(alias, 'command').split())})
    return output