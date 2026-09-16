def _parse_phone(self, val):
    ret = {'type': None, 'value': None}
    try:
        ret['type'] = val[1]['type']
    except (IndexError, KeyError, ValueError, TypeError):
        pass
    ret['value'] = val[3].strip()
    try:
        self.vars['phone'].append(ret)
    except AttributeError:
        self.vars['phone'] = []
        self.vars['phone'].append(ret)