def param_extract(args, short_form, long_form, default=None):
    val = default
    for i, a in enumerate(args):
        elems = a.split('=', 1)
        if elems[0] in [short_form, long_form]:
            if len(elems) == 1:
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    val = args[i + 1]
                else:
                    val = ''
            else:
                val = elems[1]
            break
    return val