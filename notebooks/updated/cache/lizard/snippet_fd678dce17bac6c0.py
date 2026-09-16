def _format_options_usage(options):
    options_usage = ''
    for op in options:
        short, long = op.get_flags()
        if op.arg:
            flag = '{short} {arg} {long}={arg}'.format(short=short, long=
                long, arg=op.arg)
        else:
            flag = '{short} {long}'.format(short=short, long=long)
        wrapped_description = textwrap.wrap(inspect.cleandoc(op.__doc__),
            width=79, initial_indent=' ' * 32, subsequent_indent=' ' * 32)
        wrapped_description = '\n'.join(wrapped_description).strip()
        options_usage += '  {0:28}  {1}\n'.format(flag, wrapped_description)
    return options_usage