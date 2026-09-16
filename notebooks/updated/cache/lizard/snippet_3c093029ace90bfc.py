def read_route_line(route):
    scrf_patt = re.compile('^([sS][cC][rR][fF])\\s*=\\s*(.+)')
    multi_params_patt = re.compile('^([A-z]+[0-9]*)[\\s=]+\\((.*)\\)$')
    functional = None
    basis_set = None
    route_params = {}
    dieze_tag = None
    if route:
        if '/' in route:
            tok = route.split('/')
            functional = tok[0].split()[-1]
            basis_set = tok[1].split()[0]
            for tok in [functional, basis_set, '/']:
                route = route.replace(tok, '')
        for tok in route.split():
            if scrf_patt.match(tok):
                m = scrf_patt.match(tok)
                route_params[m.group(1)] = m.group(2)
            elif tok.upper() in ['#', '#N', '#P', '#T']:
                if tok == '#':
                    dieze_tag = '#N'
                else:
                    dieze_tag = tok
                continue
            else:
                m = re.match(multi_params_patt, tok.strip('#'))
                if m:
                    pars = {}
                    for par in m.group(2).split(','):
                        p = par.split('=')
                        pars[p[0]] = None if len(p) == 1 else p[1]
                    route_params[m.group(1)] = pars
                else:
                    d = tok.strip('#').split('=')
                    route_params[d[0]] = None if len(d) == 1 else d[1]
    return functional, basis_set, route_params, dieze_tag