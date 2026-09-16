def json_options_to_metadata(options, add_brackets=True):
    try:
        options = loads('{' + options + '}' if add_brackets else options)
        return options
    except ValueError:
        return {}