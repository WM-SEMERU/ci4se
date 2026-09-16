def clipstr(s, dispw):
    w = 0
    ret = ''
    ambig_width = options.disp_ambig_width
    for c in s:
        if c != ' ' and unicodedata.category(c) in ('Cc', 'Zs', 'Zl'):
            c = options.disp_oddspace
        if c:
            c = c[0]
            ret += c
            eaw = unicodedata.east_asian_width(c)
            if eaw == 'A':
                w += ambig_width
            elif eaw in 'WF':
                w += 2
            elif not unicodedata.combining(c):
                w += 1
        if w > dispw - len(options.disp_truncator) + 1:
            ret = ret[:-2] + options.disp_truncator
            w += len(options.disp_truncator)
            break
    return ret, w