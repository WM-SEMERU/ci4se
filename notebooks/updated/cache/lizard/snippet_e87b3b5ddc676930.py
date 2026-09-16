def _format_subcommand(command):
    yield '.. object:: {}'.format(command.name)
    if CLICK_VERSION < (7, 0):
        short_help = command.short_help
    else:
        short_help = command.get_short_help_str()
    if short_help:
        yield ''
        for line in statemachine.string2lines(short_help, tab_width=4,
            convert_whitespace=True):
            yield _indent(line)