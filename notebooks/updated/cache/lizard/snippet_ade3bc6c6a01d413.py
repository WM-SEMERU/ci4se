def parser_help_text(help_text):
    if help_text is None:
        return None, {}
    main_text = ''
    params_help = {}
    for line in help_text.splitlines():
        line = line.strip()
        match = re.search(':\\s*param\\s*(?P<param>\\w+)\\s*:(?P<help>.*)$',
            line)
        if match:
            params_help[match.group('param')] = match.group('help').strip()
        else:
            main_text += line + ' '
    main_text = main_text.strip()
    return main_text, params_help