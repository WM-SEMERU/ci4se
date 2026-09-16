def expand_variables(self, message):
    p = copy.deepcopy(self.data)
    if 'to_from' in self.data:
        to_from = self.data['to_from'].copy()
        to_from['url'] = to_from['url'].format(**message)
        if 'expr' in to_from:
            to_from['expr'] = to_from['expr'].format(**message)
        p.setdefault('to', []).extend(ValuesFrom(to_from, self.manager).
            get_values())
    if 'cc_from' in self.data:
        cc_from = self.data['cc_from'].copy()
        cc_from['url'] = cc_from['url'].format(**message)
        if 'expr' in cc_from:
            cc_from['expr'] = cc_from['expr'].format(**message)
        p.setdefault('cc', []).extend(ValuesFrom(cc_from, self.manager).
            get_values())
    return p