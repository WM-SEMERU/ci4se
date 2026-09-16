def tokenize(cls, obj):
    tokens = {}
    try:
        token_iterator = cls.make_iterable(obj)
        _lang = cls.language_definition()
        tokens = {k: [] for k in _lang.argument_types}
        prev, current = None, next(token_iterator)
        while True:
            token = [None, None]
            arg_type = None
            for arg_type in _lang.argument_types:
                arg_start_seq = _lang.argument_types[arg_type]
                arg_delimiters = _lang.value_delimiters[arg_type]
                if prev is None and arg_start_seq is None:
                    token[1] = current
                    break
                elif arg_start_seq is None and prev[0] is None:
                    token[1] = current
                    break
                elif arg_start_seq is None and prev[0] is not None:
                    token[1] = current
                    break
                elif arg_start_seq is None:
                    prev[1] = current
                    token = None
                    break
                elif current[:len(arg_start_seq)] == arg_start_seq:
                    token[0] = current[len(arg_start_seq):]
                    for delimiter in arg_delimiters:
                        if delimiter == ' ':
                            continue
                        if delimiter in token[0]:
                            _delim = str(token[0]).partition(delimiter)
                            token = [_delim[0], _delim[2]]
                            break
                    break
            if token:
                tokens[arg_type].append(token)
            prev, current = token, next(token_iterator)
    except StopIteration:
        return tokens