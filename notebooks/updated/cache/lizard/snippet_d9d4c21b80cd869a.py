def print_params(self, allpars=False, loglevel=logging.INFO):
    pars = self.get_params()
    o = '\n'
    o += '%4s %-20s%10s%10s%10s%10s%10s%5s\n' % ('idx', 'parname', 'value',
        'error', 'min', 'max', 'scale', 'free')
    o += '-' * 80 + '\n'
    src_pars = collections.OrderedDict()
    for p in pars:
        src_pars.setdefault(p['src_name'], [])
        src_pars[p['src_name']] += [p]
    free_sources = []
    for k, v in src_pars.items():
        for p in v:
            if not p['free']:
                continue
            free_sources += [k]
    for k, v in src_pars.items():
        if not allpars and k not in free_sources:
            continue
        o += '%s\n' % k
        for p in v:
            o += '%4i %-20.19s' % (p['idx'], p['par_name'])
            o += '%10.3g%10.3g' % (p['value'], p['error'])
            o += '%10.3g%10.3g%10.3g' % (p['min'], p['max'], p['scale'])
            if p['free']:
                o += '    *'
            else:
                o += '     '
            o += '\n'
    self.logger.log(loglevel, o)