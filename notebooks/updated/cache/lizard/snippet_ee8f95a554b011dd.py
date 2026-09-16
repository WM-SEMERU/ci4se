def generate_documentation(schema):
    documentation_title = 'Configuration documentation'
    documentation = documentation_title + '\n'
    documentation += '=' * len(documentation_title) + '\n'
    for section_name in schema:
        section_created = False
        for option_name in schema[section_name]:
            option = schema[section_name][option_name]
            if not section_created:
                documentation += '\n'
                documentation += section_name + '\n'
                documentation += '-' * len(section_name) + '\n'
                section_created = True
            documentation += '\n'
            documentation += option_name + '\n'
            documentation += '~' * len(option_name) + '\n'
            if option.get('required'):
                documentation += '** This option is required! **\n'
            if option.get('type'):
                documentation += '*Type : %s.*\n' % option.get('type')
            if option.get('description'):
                documentation += option.get('description') + '\n'
            if option.get('default'):
                documentation += 'The default value is %s.\n' % option.get(
                    'default')
            if option.get('deprecated'):
                documentation += '** This option is deprecated! **\n'
    return documentation