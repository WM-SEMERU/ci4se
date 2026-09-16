def list_state_functions(*args, **kwargs):
    st_ = salt.state.State(__opts__)
    if not args:
        return sorted(st_.states)
    names = set()
    for module in args:
        if '*' in module or '.' in module:
            for func in fnmatch.filter(st_.states, module):
                names.add(func)
        else:
            moduledot = module + '.'
            for func in st_.states:
                if func.startswith(moduledot):
                    names.add(func)
    return sorted(names)