def join_locale(comps):
    loc = comps['language']
    if comps.get('territory'):
        loc += '_' + comps['territory']
    if comps.get('codeset'):
        loc += '.' + comps['codeset']
    if comps.get('modifier'):
        loc += '@' + comps['modifier']
    if comps.get('charmap'):
        loc += ' ' + comps['charmap']
    return loc