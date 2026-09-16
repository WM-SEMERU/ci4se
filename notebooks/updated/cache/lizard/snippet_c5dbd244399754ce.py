def autocomplete(input_list):
    if input_list[0] in ['modulehelp', 'enable', 'disable']:
        commands = []
        for modulename in seash_modules.module_data.keys():
            commands.append(input_list[0] + ' ' + modulename)
        return commands
    return []