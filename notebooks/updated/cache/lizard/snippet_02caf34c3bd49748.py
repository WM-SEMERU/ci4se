def _printable_id_code(self):
    code = super(ISWCCode, self)._printable_id_code()
    code1 = code[:3]
    code2 = code[3:6]
    code3 = code[-3:]
    return '%s.%s.%s' % (code1, code2, code3)