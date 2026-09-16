def state_doc(*args):
    st_ = salt.state.State(__opts__)
    docs = {}
    if not args:
        for fun in st_.states:
            state = fun.split('.')[0]
            if state not in docs:
                if hasattr(st_.states[fun], '__globals__'):
                    docs[state] = st_.states[fun].__globals__['__doc__']
            docs[fun] = st_.states[fun].__doc__
        return _strip_rst(docs)
    for module in args:
        _use_fnmatch = False
        if '*' in module:
            target_mod = module
            _use_fnmatch = True
        elif module:
            target_mod = module + '.' if not module.endswith('.') else module
        else:
            target_mod = ''
        if _use_fnmatch:
            for fun in fnmatch.filter(st_.states, target_mod):
                state = fun.split('.')[0]
                if hasattr(st_.states[fun], '__globals__'):
                    docs[state] = st_.states[fun].__globals__['__doc__']
                docs[fun] = st_.states[fun].__doc__
        else:
            for fun in st_.states:
                if fun == module or fun.startswith(target_mod):
                    state = module.split('.')[0]
                    if state not in docs:
                        if hasattr(st_.states[fun], '__globals__'):
                            docs[state] = st_.states[fun].__globals__['__doc__'
                                ]
                    docs[fun] = st_.states[fun].__doc__
    return _strip_rst(docs)