def find_depth(data, s='', level=None):
    _s = re.compile('^' + _escape_regexp(s.rstrip('*')))
    _p = re.compile('\\|')

    def _count_pipes(val):
        return len(_p.findall(re.sub(_s, '', val))) if _s.match(val) else None
    n_pipes = map(_count_pipes, data)
    if level is None:
        return list(n_pipes)
    if not isstr(level):
        test = lambda x: level == x if x is not None else False
    elif level[-1] == '-':
        level = int(level[:-1])
        test = lambda x: level >= x if x is not None else False
    elif level[-1] == '+':
        level = int(level[:-1])
        test = lambda x: level <= x if x is not None else False
    else:
        raise ValueError('Unknown level type: `{}`'.format(level))
    return list(map(test, n_pipes))