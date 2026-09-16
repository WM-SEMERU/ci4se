def _print_context(filename, secret, count, total, plugin_settings,
    additional_header_lines=None, force=False):
    print('{} {} {} {}\n{} {}\n{} {}'.format(colorize('Secret:     ',
        AnsiColor.BOLD), colorize(str(count), AnsiColor.PURPLE), colorize(
        'of', AnsiColor.BOLD), colorize(str(total), AnsiColor.PURPLE),
        colorize('Filename:   ', AnsiColor.BOLD), colorize(filename,
        AnsiColor.PURPLE), colorize('Secret Type:', AnsiColor.BOLD),
        colorize(secret['type'], AnsiColor.PURPLE)))
    if additional_header_lines:
        print(additional_header_lines)
    print('-' * 10)
    error_obj = None
    try:
        secret_with_context = _get_secret_with_context(filename, secret,
            plugin_settings, force=force)
        print(secret_with_context)
    except SecretNotFoundOnSpecifiedLineError as e:
        error_obj = e
        print(e)
    print('-' * 10)
    if error_obj:
        raise error_obj