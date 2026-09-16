def parse_arg_line(fargs):
    fargs = fargs.strip()
    if fargs == '':
        return {}
    pairs = [s.strip() for s in fargs.split(',')]
    result = []
    for p in pairs:
        fe = p.find('=')
        if fe == -1:
            raise ValueError('malformed')
        key = p[:fe]
        val = p[fe + 1:]
        tok = "'{}': {}".format(key, val)
        result.append(tok)
    tokj = ','.join(result)
    result = '{{ {0} }}'.format(tokj)
    state = ast.literal_eval(result)
    return state