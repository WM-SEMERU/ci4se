def _isbool(string):
    return isinstance(string, _bool_type) or isinstance(string, (
        _binary_type, _text_type)) and string in ('True', 'False')