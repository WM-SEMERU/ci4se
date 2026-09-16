def list_styles(style_name):
    style = get_style_by_name(style_name)
    keys = list(style)[0][1]
    Styles = namedtuple('Style', keys)
    existing_styles = {}
    for ttype, ndef in style:
        s = Styles(**ndef)
        if s in existing_styles:
            existing_styles[s].append(ttype)
        else:
            existing_styles[s] = [ttype]
    for ndef, ttypes in existing_styles.items():
        print(ndef)
        for ttype in sorted(ttypes):
            print('\t%s' % str(ttype).split('Token.', 1)[1])