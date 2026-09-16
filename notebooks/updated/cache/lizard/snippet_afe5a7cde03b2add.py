def convert_markerstyle(inputstyle, mode, inputmode=None):
    mode = mode.lower()
    if mode not in ('mpl', 'root'):
        raise ValueError('`{0}` is not valid `mode`'.format(mode))
    if inputmode is None:
        if inputstyle in markerstyles_root2mpl:
            inputmode = 'root'
        elif inputstyle in markerstyles_mpl2root or '$' in str(inputstyle):
            inputmode = 'mpl'
        elif inputstyle in markerstyles_text2root:
            inputmode = 'root'
            inputstyle = markerstyles_text2root[inputstyle]
        else:
            raise ValueError('`{0}` is not a valid `markerstyle`'.format(
                inputstyle))
    if inputmode == 'root':
        if inputstyle not in markerstyles_root2mpl:
            raise ValueError('`{0}` is not a valid ROOT `markerstyle`'.
                format(inputstyle))
        if mode == 'root':
            return inputstyle
        return markerstyles_root2mpl[inputstyle]
    else:
        if '$' in str(inputstyle):
            if mode == 'root':
                return 1
            else:
                return inputstyle
        if inputstyle not in markerstyles_mpl2root:
            raise ValueError('`{0}` is not a valid matplotlib `markerstyle`'
                .format(inputstyle))
        if mode == 'mpl':
            return inputstyle
        return markerstyles_mpl2root[inputstyle]