def render_unicode_sub_super(name, subs=None, supers=None, sub_first=True,
    translate_symbols=True, unicode_sub_super=True, sep=',',
    subscript_max_len=1):
    if subs is None:
        subs = []
    if supers is None:
        supers = []
    if translate_symbols:
        supers = [_translate_symbols(sup) for sup in supers]
        subs = [_translate_symbols(sub) for sub in subs]
        name = _translate_symbols(name)
    res = name
    try:
        if unicode_sub_super:
            supers_modified = [_unicode_sub_super(s, _SUPERSCRIPT_MAPPING) for
                s in supers]
            subs_modified = [_unicode_sub_super(s, _SUBSCRIPT_MAPPING,
                max_len=subscript_max_len) for s in subs]
            if sub_first:
                if len(subs_modified) > 0:
                    res += sep.join(subs_modified)
                if len(supers_modified) > 0:
                    res += sep.join(supers_modified)
            else:
                if len(supers_modified) > 0:
                    res += sep.join(supers_modified)
                if len(subs_modified) > 0:
                    res += sep.join(subs_modified)
    except KeyError:
        unicode_sub_super = False
    if not unicode_sub_super:
        sub = sep.join(subs)
        sup = sep.join(supers)
        if sub_first:
            if len(sub) > 0:
                res += '_%s' % sub
            if len(sup) > 0:
                res += '^%s' % sup
        else:
            if len(sup) > 0:
                res += '^%s' % sup
            if len(sub) > 0:
                res += '_%s' % sub
    return res