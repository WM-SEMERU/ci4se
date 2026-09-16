def all_to_intermediary(filename_or_input, schema=None):
    input_class_name = filename_or_input.__class__.__name__
    try:
        this_to_intermediary = switch_input_class_to_method[input_class_name]
        tables, relationships = this_to_intermediary(filename_or_input)
        return tables, relationships
    except KeyError:
        pass
    if isinstance(filename_or_input, basestring):
        if filename_or_input.split('.')[-1] == 'er':
            return markdown_file_to_intermediary(filename_or_input)
    if not isinstance(filename_or_input, basestring):
        if all(isinstance(e, basestring) for e in filename_or_input):
            return line_iterator_to_intermediary(filename_or_input)
    try:
        make_url(filename_or_input)
        return database_to_intermediary(filename_or_input, schema=schema)
    except ArgumentError:
        pass
    msg = 'Cannot process filename_or_input {}'.format(input_class_name)
    raise ValueError(msg)