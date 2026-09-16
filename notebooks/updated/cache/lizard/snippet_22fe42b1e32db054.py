def get_tokendefs(cls):
    tokens = {}
    inheritable = {}
    for c in cls.__mro__:
        toks = c.__dict__.get('tokens', {})
        for state, items in iteritems(toks):
            curitems = tokens.get(state)
            if curitems is None:
                tokens[state] = items
                try:
                    inherit_ndx = items.index(inherit)
                except ValueError:
                    continue
                inheritable[state] = inherit_ndx
                continue
            inherit_ndx = inheritable.pop(state, None)
            if inherit_ndx is None:
                continue
            curitems[inherit_ndx:inherit_ndx + 1] = items
            try:
                new_inh_ndx = items.index(inherit)
            except ValueError:
                pass
            else:
                inheritable[state] = inherit_ndx + new_inh_ndx
    return tokens