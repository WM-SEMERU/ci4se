def __stringify_predicate(predicate):
    funname = getsource(predicate).strip().split(' ')[2].rstrip(',')
    params = 'None'
    if '()' not in funname:
        stack = getouterframes(currentframe())
        for frame in range(0, len(stack)):
            if funname in str(stack[frame]):
                _, _, _, params = getargvalues(stack[frame][0])
    return 'function: {} params: {}'.format(funname, params)