def parse_path(nstr):
    if not nstr:
        return []
    n = nstr.split('/')
    if n[0] == 'm':
        n = n[1:]

    def str_to_harden(x):
        if x.startswith('-'):
            return H_(abs(int(x)))
        elif x.endswith(('h', "'")):
            return H_(int(x[:-1]))
        else:
            return int(x)
    try:
        return list(str_to_harden(x) for x in n)
    except Exception:
        raise ValueError('Invalid BIP32 path', nstr)