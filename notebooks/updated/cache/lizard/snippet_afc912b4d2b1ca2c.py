def _prepare_doc(func, args, delimiter_chars):
    _LOG.debug("Preparing doc for '%s'", func.__name__)
    if not func.__doc__:
        return _get_default_help_message(func, args)
    description = []
    args_help = {}
    fill_description = True
    arg_name = None
    arg_doc_regex = re.compile(
        '\x08*(?P<arg_name>\\w+)\\s*%s\\s*(?P<help_msg>.+)' % delimiter_chars)
    for line in func.__doc__.splitlines():
        line = line.strip()
        if line and fill_description:
            description.append(line)
        elif line:
            arg_match = arg_doc_regex.match(line)
            try:
                arg_name = arg_match.groupdict()['arg_name'].strip()
                args_help[arg_name] = arg_match.groupdict()['help_msg'].strip()
            except AttributeError:
                if arg_name is not None:
                    args_help[arg_name] = ' '.join([args_help[arg_name], line])
        else:
            if not fill_description and args_help:
                break
            fill_description = False
    return _get_default_help_message(func, args, ' '.join(description),
        args_help)