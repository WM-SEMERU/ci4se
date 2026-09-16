def max_width(*args, **kwargs):
    args = list(args)
    if not args:
        args.append(kwargs.get('string'))
        args.append(kwargs.get('cols'))
        args.append(kwargs.get('separator'))
    elif len(args) == 1:
        args.append(kwargs.get('cols'))
        args.append(kwargs.get('separator'))
    elif len(args) == 2:
        args.append(kwargs.get('separator'))
    string, cols, separator = args
    if separator is None:
        separator = '\n'
    if cols is None:
        string, cols = cols, string
    if string is None:
        MAX_WIDTHS.append((cols, separator))
        return _max_width_context()
    else:
        return _max_width_formatter(string, cols, separator)