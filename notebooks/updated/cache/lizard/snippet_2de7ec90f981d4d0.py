def str_arg(d):
    if not d:
        return None
    if isinstance(d, dict):
        if len(d) == 2 and d.get('type') == 'text' and 'value' in d:
            return str_arg(d['value'])
        if len(d) == 2 and d.get('type') == 'text' and 'subkey' in d:
            return '.%s' % d['subkey']
        if d.get('type') == 'module':
            return None
        return '{%s}' % str_args(d.items())
    if isinstance(d, list):
        if len(d) == 1:
            return str_arg(d[0])
        return '[%s]' % ', '.join(str_arg(elem) for elem in d)
    if isinstance(d, unicode):
        return '"%s"' % d
    return repr(d)